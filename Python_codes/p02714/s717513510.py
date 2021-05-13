n = int(input())
s = input()

rs = s.count('R')
gs = s.count('G')
bs = s.count('B')

t = rs * gs * bs

for i in range(n-2):
    for j in range(i, n-1):
        k = 2 * j - i
        if k < n:
            if s[i] != s[j] and s[j] != s[k] and s[k] != s[i]:
                t -= 1

print(t)
