n = int(input())
h = list(map(int,input().split()))

ans = []
now = 0

for i in range(1,n):
    if h[i-1] >= h[i]:
        now += 1
    else:
        ans.append(now)
        now = 0

ans.append(now)

print(max(ans))
