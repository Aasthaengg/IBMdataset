



from collections import defaultdict

N = int(input())


"""
愚直解だと、Aを1~Nまで動かした時、各Aについて何個Bを取れるかを足し合わせると答えが出る。が、これはN<=2*10**5なのでO(N^2)は間に合わない。

事前に先頭がxで末尾がyの個数を、1~Nまで数え上げておくと、各Aについて先頭と末尾を抜き出して、それに対応するBの個数を足し合わせるとO(N)で求められる
"""
d = defaultdict(int)



for i in range(1,N+1):
    d[(int(str(i)[0]), int(str(i)[-1]))] += 1


ans = 0
for a in range(1,N+1):
    x = int(str(a)[0])
    y = int(str(a)[-1])
    ans += d[(y,x)]

print(ans)