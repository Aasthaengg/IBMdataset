n, k, c = map(int, input().split())
s = input()
l = []
r = []
i = 0
while len(l) < k:
    if s[i] == 'o':
        l.append(i)
        i += c + 1
    else:
        i += 1

i = n - 1
while len(r) < k:
    if s[i] == 'o':
        r.append(i)
        i -= c + 1
    else:
        i -= 1

r = r[::-1]

for i, j in zip(l, r):
    if i == j:
        print(i + 1)
