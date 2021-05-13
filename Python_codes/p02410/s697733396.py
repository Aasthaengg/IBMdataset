n, m = map(int, input().split())

a = [0] * n 
for i in range(n):
    a[i] = list(map(int, input().split()))

b = [0] * m
for i in range(m):
    b[i] = int(input())

c = [0] * n    
for i in range(n):
    for aj, bj in zip(a[i], b):
        c[i] += aj * bj
    
for ci in c:
    print(ci)