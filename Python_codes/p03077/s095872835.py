N = int(input())
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

m = 10**15+5
min_arg = 0
for i, j in enumerate([a,b,c,d,e], 1):
    if j < m:
        min_arg = i
        m = j

print(N//m + (N%m!=0) + 4)