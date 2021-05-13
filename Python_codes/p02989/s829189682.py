n = int(input())
d = [int(xi) for xi in input().split()]

d = sorted(d)

print(d[int(n/2)]-d[int(n/2)-1])
