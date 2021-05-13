n = int(input())
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]

c = 0
for i in range(n):
    c = max(c, sum(a[:i+1] + b[i:]))
else:
    print(c)