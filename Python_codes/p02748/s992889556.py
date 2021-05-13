A,B,M = map(int,input().split())

a =  list(map(int,input().split()))
b = list(map(int,input().split()))

min = sorted(a)[0] + sorted(b)[0]

for  i  in range(M):
    x,y,c =map(int,input().split())
    if min > a[x-1]+b[y-1]-c:
        min = a[x-1]+b[y-1]-c
            
print(min)