N = int(input())
ans = []
for i in range(N):
    d = list(map(int, input().split()))
    d.sort()
    if d[2]**2 == d[1]**2+d[0]**2:
        ans.append("YES")
    else:
        ans.append("NO")
for i in range(N):
    print(ans[i])