N = int(input())
p = q = 0
for i in range(N):
    a, b = input().split()
    if a < b:
        q += 3
    elif a > b:
        p += 3
    else:
        p += 1
        q += 1
print(p, q)
