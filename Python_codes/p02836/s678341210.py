s = input()
n = len(s)
print(len([i for i in range(n // 2) if s[i] != s[n - 1 - i]]))