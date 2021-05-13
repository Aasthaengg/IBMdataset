s = list(input())
l = int(input())
s1 = sorted(s)
ans = set()

for i in range(len(s)):
    sta = s1[i]
    for j in range(len(s)):
        if s[j] == sta:
            ans.add(s[j])
            check = s[j]
            for k in range(j+1,min(len(s),j+5)):
                check = check+s[k]
                ans.add(check)
    if len(ans) >= l:
        ans1 = sorted(ans)
        print(ans1[l-1])
        exit()
ans1 = sorted(ans)
print(ans1[l-1])