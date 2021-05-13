n, k, c = map(int, input().split())
s = list(input())

R = []
p = 0
for _ in range(k):
    while s[p] == 'x':
        p += 1
    R.append(p)
    p += c + 1

L = []
p = n - 1
for _ in range(k):
    while s[p] == 'x':
        p -= 1
    L.append(p)
    p -= c + 1

L = list(reversed(L))

for i in range(k):
    if R[i] == L[i]:
        print(R[i] + 1)
