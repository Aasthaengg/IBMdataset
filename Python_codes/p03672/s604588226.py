s = input()
for i in range((len(s) >> 1) - 1, -1, -1):
    n = i << 1
    if s[:i] == s[i:n]:
        print(n)
        break