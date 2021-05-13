s = str(input())
n, g, p = len(s), s.count('g'), s.count('p')

print(g - (n - n // 2))
