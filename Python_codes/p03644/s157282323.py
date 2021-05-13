n = int(input())
l = []

for i in range(1001):
    l.append(2**i)

最大 = 0
for i in range(n+1):
    if i in l:
        最大 = i

print(最大)