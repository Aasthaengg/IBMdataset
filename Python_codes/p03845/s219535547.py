from copy import copy
n = int(input())
t = list(map(int, input().split()))
m = int(input())

for i in range(m):
    p, x = map(int, input().split())
    c = copy(t)
    c[p-1] = x
    print(sum(c))
