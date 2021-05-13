n = int(input())
k = int(input())

l = list()

for bit in range((1 << n)+1):
    num = 1
    for i in range(n):
        if bit & (1 << i):
            num *= 2
        else:
            num += k
    l.append(num)

print(min(l))
