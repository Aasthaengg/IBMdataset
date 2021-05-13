import bisect

n = int(input())

L = list(map(int,input().split()))

A = sorted(L)

ans = 0

for i in range(n):
    for j in range(i+1,n):
        total = L[i] + L[j]
        ans += bisect.bisect_left(A,total) - (j+1)

print(ans)  
