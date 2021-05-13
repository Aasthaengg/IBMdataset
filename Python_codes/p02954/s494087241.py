s = input()
n = len(s)
l = [1]*n

for i in range(n - 1):
    if s[i] == s[i + 1] == "R":
        l[i + 2] += l[i]
        l[i] = 0
    if s[-i - 1] == s[-i - 2] == "L":
        l[-i - 3] += l[-i - 1]
        l[-i - 1] = 0

print(*l)