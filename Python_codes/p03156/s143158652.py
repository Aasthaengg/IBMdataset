n = int(input())
a, b = map(int, input().split())
p = list(map(int, input().split()))

c1 = 0
c2 = 0
c3 = 0

for pi in p:
    if pi <= a:
        c1 += 1
    elif pi <= b:
        c2 += 1
    else:
        c3 += 1

print(min(c1, c2, c3))
