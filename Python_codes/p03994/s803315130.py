s = input()
k = int(input())
l = "abcdefghijklmnopqrstuvwxyz"
ans = ""
for i in range(len(s) - 1):
    num = (26 - l.index(s[i])) % 26
    if k >= num:
        ans += "a"
        k -= num
    else:
        ans += s[i]
ans += l[(l.index(s[-1]) + k) % 26]
print(ans)