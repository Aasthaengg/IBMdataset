a, b = map(int,input().split())
s = ""
sn = ""
ans = 0
for i in range(a,b+1):
    s = str(i)
    sn = s[::-1]
    if s == sn:
        ans += 1
print(ans)
