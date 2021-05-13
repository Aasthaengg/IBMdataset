n = int(input())
a = list(map(int,input().split()))
star = 0
ans = [0 for i in range(n)]
for i in range(n):
    star += a[i]
for i in range((n-1)//2):
    ans[0] += 2*a[2*i+1]
    ans[1] += 2*a[2*i+2]
ans[0] = star-ans[0]
ans[1] = star-ans[1]
for i in range(1,n//2):
    ans[2*i] = ans[2*(i-1)] + 2*a[2*(i-1)+1] - 2*a[2*(i-1)]
    ans[2*i+1] = ans[2*(i-1)+1] + 2*a[2*(i-1)+2] - 2*a[2*(i-1)+1]
ans[n-1] = ans[n-3] + 2*a[n-2]  - 2*a[n-3]
for i in range(n):
    print(ans[i],end=' ')