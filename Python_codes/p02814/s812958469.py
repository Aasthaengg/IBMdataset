'''ika tako
小数が出てくるとややこしいが、 (A)bi=ai/2  として、 
X=bi*(2p+1)  としてしまえばいい。
これで、以下の2つを満たせばよいことがわかりやすくなる。
X  は全ての  bi  の公倍数
X  を  bi  で割った商は全て奇数
なので、とりあえず全ての  bi  の最小公倍数を求めて、
それが  bi  で割ると全て奇数となるか確認する。(B)
1つでも偶数となるものがあれば、達成不可能。
全て奇数なら、最小公倍数の奇数倍が全て条件を満たす。
2数  n,m  の最小公倍数は、最大公約数を  g  として  
n*m/g  で求められる。(D)
3数以上なら、これを繰り返し適用しつづければよい。
ただし  bi  が互いに素だと、最小公倍数は繰り返している内に
とてつもなく大きくなってしまう。途中で  M  以上になった時点で (C)
M  以下の半公倍数は不可能なので、0を出力して即終了する。
'''
from fractions import gcd#最大公約数を求める関数
 
def solve(n, m, aaa):
    lcm = 1
    for a in aaa:
        a //= 2#aは、上記biに相当する変数に変換(A)
        lcm *= a // gcd(lcm, a) 
        #最小公倍数を求める、上記n*m/g に相当(D)
        if lcm > m:#最小公倍数が上限mを上回ったら解なし (C)
            return 0
    for a in aaa:
        if int(lcm / a) == lcm / a:#割り切れたら等式成立
            return 0#上記bi  で割った時に、奇数にならないケース(B)
    return (m // lcm + 1) // 2

n, m = list(map(int, input().split()))
aaa = list(map(int, input().split()))
 
print(solve(n, m, aaa))