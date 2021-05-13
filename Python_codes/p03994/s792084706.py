s = input()
k = int(input())
ans = ""
for i in s:
    if k >= (123 - ord(i)) % 26:
        k -= (123 - ord(i)) % 26
        ans += "a"
    else:
        ans += i
print(ans[:-1] + chr((ord(ans[-1]) - 97 + k) % 26 + 97))