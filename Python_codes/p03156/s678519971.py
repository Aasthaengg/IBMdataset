n = int(input())
a, b = map(int, input().split())
p = list(map(int, input().split()))

c1, c2, c3 = 0, 0, 0

for i in p:
    if i <= a:
        c1 += 1
    elif a < i <= b:
        c2 += 1
    elif b < i:
        c3 += 1

print(min(c1, c2, c3))