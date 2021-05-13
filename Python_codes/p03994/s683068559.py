s = input()
k = int(input())

ans = []

for i in range(len(s)):
    if 123 - ord(s[i]) <= k:
        if s[i] == "a":
            ans.append("a")
            continue
        ans.append("a")
        k -= 123 - ord(s[i])
    else:
        ans.append(s[i])

last = chr((ord(ans[-1])-97+k)%26 + 97)
ans[-1] = last


print(*ans, sep = "")
