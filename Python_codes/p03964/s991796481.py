n = int(input())

a,b = map(int, input().split())

for _ in range(n-1):
    c,d = map(int, input().split())
    i = (a+c-1)//c
    j = (b+d-1)//d
    k = max(i,j)
    a = c*k
    b = d*k
print(a+b)
