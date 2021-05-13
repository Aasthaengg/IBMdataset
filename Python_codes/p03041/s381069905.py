n, k = map(int, input().split())
s = input()

new = ""
for i in range(len(s)):
    if i == k-1:
        new += s[i].lower()
    else:
        new += s[i]

print(new)