n = int(input())
s = input()
ans = ""

for i in range(len(s)):
    a = ord(s[i]) + n
    if a <= ord("Z"):
        ans += chr(a)
    else:
        ans += chr(a - 26)

print(ans)