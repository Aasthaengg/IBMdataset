s = input()
a = s[::-1]
n = len(s)
ans = "Yes"
if s != a: ans = "No"
elif s[:(n-1)//2] != s[(n+3)//2-1:]: ans = "No"
print(ans)