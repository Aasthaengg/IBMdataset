s = list(input())

for i in range(len(s)):
    if s[i] == 'C'or s[i] == 'G' or s[i] == 'T':
        s[i] = 'A'

s = ''.join(s)
n = s.count('A')

for i in range(n+1)[::-1]:
    if 'A' * i in s:
        print(i)
        break
else:
    print(0)