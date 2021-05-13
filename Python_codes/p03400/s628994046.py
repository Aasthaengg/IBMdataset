s = input()
n = int(s)

v = input().split()
d = int(v[0])
x = int(v[1])

eats = 0

for i in range(n):
    p = input()
    q = int(p)
    c = 1
    while (c <= d):
        eats += 1
        c += q

answer = eats + x
print(answer)