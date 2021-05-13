a, b, c = map(int, input().split())

l = [a + b, a + c, b + c]

min = l[0]

for i in l:
    if min > i:
        min = i

print(min)
