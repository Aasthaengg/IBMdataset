a,b,k = map(int,input().split())

for i in range(k//2):
    a,b = a//2,b+a//2
    b,a = b//2,a+b//2

if k%2==1:
    a,b = a//2,b+a//2

print(a,b)
