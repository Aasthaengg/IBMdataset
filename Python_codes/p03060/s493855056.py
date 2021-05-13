n = int(input())
v = [int(i) for i in input().split()]
c = [int(i) for i in input().split()]


maximum = 0
profit = []
for i in range(len(v)):
    tmp = v[i] - c[i]
    if tmp > 0:
        maximum += tmp
    tmp = 0

print(maximum)
