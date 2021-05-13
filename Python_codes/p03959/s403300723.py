mod = 10**9+7
import sys

N = int(input())

T = list(map(int,input().split()))
A = list(map(int,input().split()))

able = [0] * N
dif = [False] * N

for i in range(N):

    able[i] = min(T[i],A[i])

for i in range(N):

    if i == 0 or T[i] != T[i-1]:
        dif[i] = True

        if A[i] < T[i]:
            print (0)
            sys.exit()

for i in range(N):
    if i == N-1 or A[i] != A[i+1]:

        if dif[i]:
            if T[i] != A[i]:
                print (0)
                sys.exit()

        else:
            if A[i] > T[i]:
                print (0)
                sys.exit()
        
        dif[i] = True

ans = 1
for i in range(N):

    if dif[i]:
        continue

    ans *= able[i]
    ans %= mod

print (ans)