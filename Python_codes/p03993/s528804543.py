N = int(input())
a = list(map(int,input().split()))
ans = 0
for k in range(N):
    if a[a[k]-1] == k+1:
        ans += 1
print(ans//2)
