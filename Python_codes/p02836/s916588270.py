s = input()
a = len(s)-sum(s[i] == s[::-1][i] for i in range(len(s)))
print(a//2)
