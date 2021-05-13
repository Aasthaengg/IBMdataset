s = input()
k = int(input())
ans = ""
l = 26
for i in range(len(s)-1):
    if l - ord(s[i]) + 97 <= k and s[i] != "a":
        k -= l - ord(s[i]) + 97
        ans += "a"
    else:
        ans += s[i]
ans += (chr(((ord(s[-1]) - 97) + k + l) % l + 97))
print(ans)