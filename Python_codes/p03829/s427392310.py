n , a , b = map(int, input().split())
x = list(map(int,input().split()))
c = 0

for i in range(n-1):
    if (x[i+1]-x[i])*a<b:
        c+=(x[i+1]-x[i])*a
    else:
        c+=b
print(c)
