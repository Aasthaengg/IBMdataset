n = int(input())
a = list(map(int, input().split()))
b = []
for i in a:
    c = 0
    while i % 2 == 0:
        c += 1
        i /= 2
    b.append(c)
print(min(b))