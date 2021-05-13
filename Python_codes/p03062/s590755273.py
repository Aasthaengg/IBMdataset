n = int(input())
a = list(map(int, input().split()))

s = 0

b = [abs(x) for x in a]

c = 0
for x in a:
    if x < 0:
        c += 1

if c % 2 == 0:
    s = sum(b)
else:
    s = sum(b) - 2 * min(b)

print(s)