s = input()

n = len(s)
ans = [0]*n
boundary = []

for i in range(n-1):
    if s[i]=='L' and s[i+1]=='R':
        boundary.append(i)
boundary.append(n-1)

l = 0
for r in boundary:
    middle = 0
    cnt = [0,0]
    for x in range(l,r+1):
        cnt[x%2] += 1
        if s[x]=='R' and s[x+1]=='L':
            middle = x

    ans[middle] = cnt[middle%2]
    ans[middle+1] = cnt[1-(middle%2)]

    l = r+1
print(*ans)