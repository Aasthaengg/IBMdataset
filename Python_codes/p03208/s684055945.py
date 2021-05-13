n,k = map(int,input().split())
l = []
for _ in range(n):
    a = int(input())
    l.append(a)

ans = 10**9
l.sort()

for i in range(n-k+1):
    tmp = l[k+i-1] - l[i]
    if tmp < ans:
        ans = tmp

print(ans)