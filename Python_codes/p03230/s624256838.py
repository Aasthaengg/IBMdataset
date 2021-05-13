#Tenka1 Programmer Beginner Contest-D Crossing
"""
1~nまでの数字を用いて、以下の条件を満たす集合を作る。

1.1~nのそれぞれの数字はちょうど2回出現する
2.ある2つの集合を見たときに、重複する要素がちょうど1つ存在する
集合の個数・要素数は任意に決定して良い

この問題で考えるべきは、
ある2頂点に同じ要素を入れたとき、残りの要素は必ず別のものになり、
それらはまた自分と同じ要素の頂点と比べたときに必ず残りの要素が別
のものになってないといけない。

という点であり、これを達成するにはかなり厳しい制約があるはず。

まず、1.の制約より、全要素数は
2*n として求まる。
また、2.の制約より、必ず1つの頂点に頂点数-1個の要素が存在すると言える。
よって、前提として、
(2*n)%(頂点数-1) == 0
となるようなnでないと達成は不可能であり、
逆にそのようなnであれば達成可能。
頂点数はn<=10**5であることから、全探索で求めることができる。
"""
import sys
readline = sys.stdin.buffer.readline
def even(n): return 1 if n%2==0 else 0
n = int(readline())
flag = 0
for i in range(1,n+2):
    if 2*n%i== 0: #そのような頂点数が存在するかどうか
        tops = i
        if 2*n//tops == tops-1:#要素数は頂点数-1になっていなければならない
            elements = tops-1
            g = [[] for _ in range(tops)]

            mod = n
            now = 0
            now2 = 1
            for j in range(n):
                g[now].append(j+1)
                g[now2].append(j+1)
                now2 += 1
                if len(g[now]) >= elements:
                    now += 1
                    now2 = now + 1
                 

            
            flag = 1
    if flag:break

if flag:
    print("Yes")
    print(len(g))
    for i in g:
        print(len(i),*i)
else:
    print("No")