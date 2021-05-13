n = int(input())
h = list(map(int,input().split()))

ans = []
c = 0
for i in range(n-1):
    if h[i+1] <= h[i]:
        c += 1
        if i == n-2:
            ans.append(c)
    elif h[i+1] > h[i]:
        ans.append(c)
        c = 0

if not ans:
    print(0)
    exit()
print(max(ans))
