N = int(input())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))

def fact(n):
    #階乗を求める
    res = 1
    for i in range(1, n+1):
        res *= i
    return res

a = 0
#aについて
f = [False] * N
for i in range(N):
    a += (P[i]-1-f[:P[i]-1].count(True)) * fact(N-i-1) + 1
    f[P[i]-1] = True

b = 0
#bについて
f = [False] * N
for i in range(N):
    b += (Q[i]-1-f[:Q[i]-1].count(True)) * fact(N-i-1) + 1
    f[Q[i]-1] = True

print(abs(a-b))