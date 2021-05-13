s = input()
k = int(input())
ans = ""
for i in range(len(s)-1):
    cost = ord("z")+1-ord(s[i])
    if s[i] == "a" or k < cost:
        ans += s[i]
    else:
        ans += "a"
        k -= cost
c = s[-1]
k %= 26
for _ in range(k):
    if c == "z": c = "a"
    else: c = chr(ord(c)+1)
ans += c
print(ans)