s = input()
for n in range(len(s) - 2, -1, -2):
    i = n >> 1
    if s[:i] == s[i:n]:
        print(n)
        break