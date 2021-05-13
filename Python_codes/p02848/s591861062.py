n = int(input())
a = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
s = input()
l = []

for i in range(len(s)):
    j = a.index(s[i])
    j = (j + n) % 26
    l.append(a[j])

print(''.join(l))