L, R, d = map(int, input().split())

c = 0
for i in range(L, R+1, 1):
    if i < d:
        continue
    if i % d == 0:
        c += 1

print(c)