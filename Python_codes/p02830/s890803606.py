n = int(input())
s, t = map(str, input().split())
l = []

for i in range(n):
    l.extend([s[i], t[i]])

print(''.join(l))
