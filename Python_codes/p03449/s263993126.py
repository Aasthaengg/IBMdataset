n = int(input())
a1 = [int(i) for i in input().split()]
a2 = [int(i) for i in input().split()]
b1 = [0] * n
b2 = [0] * n
c1 = 0
c2 = 0
for i in range(n):
    b1[i] = c1 + a1[i]
    c1 += a1[i]
for i in range(n):
    b2[- 1 - i] = c2 + a2[- 1 - i]
    c2 += a2[- 1 - i]
d = []
for i in range(n):
    d.append(b1[i] + b2[i])
print(max(d))