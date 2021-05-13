n = int(input())
s = input()
ans = 0
for i in range(1,n):
    cnt = 0
    for m in set(s[:i]):
        if m in s[i:]:
            cnt += 1
    ans = max(ans,cnt)
print(ans)
