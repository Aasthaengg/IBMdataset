import sys
input = sys.stdin.readline

N = int(input())
T = [0]+list(map(int, input().split()))+[0]
A = [0]+list(map(int, input().split()))+[0]
ans = 1
MOD = 10**9+7

for i in range(1, N+1):
    if T[i]!=T[i-1] and A[i]!=A[i+1]:
        if T[i]!=A[i]:
            print(0)
            exit()
    elif T[i]!=T[i-1] and A[i]==A[i+1]:
        if T[i]>A[i]:
            print(0)
            exit()
    elif T[i]==T[i-1] and A[i]!=A[i+1]:
        if A[i]>T[i]:
            print(0)
            exit()
    else:
        ans *= min(T[i], A[i])
        ans %= MOD

print(ans)