
h, a = list(map(int, input().split()))

i = 0
while h > 0:
    h -= a
    i += 1
print(i)

