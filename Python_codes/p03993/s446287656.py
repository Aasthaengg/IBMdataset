n = int(input())
ans = 0
flag = [-1 for i in range(n+1)]
A = list(map(int,input().split()))
for i in range(n):
    flag[i+1] = A[i]
for i in range(1,n+1):
    if flag[flag[i]] == i:
        ans += 1
print(ans//2)