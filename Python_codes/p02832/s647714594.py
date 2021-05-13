N =  int(input())
A = list(map(int,input().split()))
n = 0

for p in range(N):
    if A[p] == n+1:
        n += 1

if n != 0:
    print(N-n)
else:
    print(-1)