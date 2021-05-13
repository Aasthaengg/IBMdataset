s = input()
ls = len(s)
ans = [1]*ls
for i in range(ls-2):
    if s[i:i+2] == "RR":
        ans[i+2] += ans[i]
        ans[i] = 0

for i in range(ls-1, 1, -1):
    if s[i-1:i+1] == "LL":
        ans[i-2] += ans[i]
        ans[i] = 0

print(*ans)