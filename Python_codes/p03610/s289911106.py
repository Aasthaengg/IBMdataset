s = input()
n = len(s)

ans = ""
for i in s[::2]:
    ans += i    

print(ans)