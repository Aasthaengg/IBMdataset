A,B,m = map(int,input().split())
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
mn = min(a)+min(b)
for i in range(m):
    x,y,c = map(int,input().split())
    res = a[x-1]+b[y-1]-c
    if mn > res:
        mn = res
print(mn)