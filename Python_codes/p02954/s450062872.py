s = input()
n  = len(s)
ans = [0]*n
rstrk = 0
lstrk = 0
for i in range(n):
    rstrk += 1
    if s[i] == "L":
        ans[i-1] += rstrk//2
        ans[i] += (rstrk+1)//2
        rstrk = 0
for i in range(n-1,-1,-1):
    lstrk += 1
    if s[i] == "R":
        ans[i+1] += lstrk//2
        ans[i] += (lstrk+1)//2
        lstrk = 0
    ans[i]-=1
print(*ans)