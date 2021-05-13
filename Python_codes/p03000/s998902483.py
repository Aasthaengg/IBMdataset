n, x = (int(xi) for xi in input().split())
l = [int(xi) for xi in input().split()]

d=0

count = 0
for xi in range(n):
    if d<x+1:
        count +=1
    d += l[xi]

if d<x+1:
    count +=1

print(count)
