s = input()
n = len(s)

ans = [1 for i in range(n)]
for i,a in enumerate(s):
    if a =="R":
        nxta = s[i+1]
        if nxta =="R":
            ans[i+2] += ans[i]
            ans[i] = 0

for i in range(n-1,-1,-1):
    a = s[i]
    if a =="L":
        nxta = s[i-1]
        if nxta =="L":
            ans[i-2] += ans[i]
            ans[i] = 0
print(*ans)
