n = int(input())
s = str(n)
ans1 =0
for i in range(len(s)):
    ans1 += int(s[i])
ans2 = (len(s)-1)*9+int(s[0])-1
print(max(ans1, ans2))
