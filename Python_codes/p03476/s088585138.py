from itertools import accumulate
import math
m = 10**5

L = [x for x in range(2,m+1)]

#エラトステネスのふるいで素数を抽出
for y in range(2, int(math.sqrt(m)+1)):
    L = [z for z in L if(z == y or z % y != 0)]

#N+1/2も素数であるものを抽出
P = []
for w in L:
    if (w+1)/2 in L:
        P.append(w)

#累積和のために作成
G = [0] * (m+1)
for i in P:
    G[i+1] = 1

#累積和
Q = list(accumulate(G))



n = int(input())
for _ in range(n):
    s, t = map(int, input().split())
    print(Q[t+1]-Q[s])




'''
この素数判定は遅い。
上のようにエラトステネスの篩を使う

def isPrime(n):

    if n == 1:
        return False
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)+1), 2):
        if n % i == 0:
            return False
    return True

'''
