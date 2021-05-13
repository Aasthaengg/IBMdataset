n = int(input())
s = list(input())
ans = ""
for i in range(len(s)):
    x = ord(s[i])+n
    if x > ord("Z"):
        x = x-ord("Z")+ord("A")-1
    ans += chr(x)
print(ans)