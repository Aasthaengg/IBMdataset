n = int(input())
a = 1
b = 1
for i in range(n):
    c,d = map(int,input().split())
    
    num = max((a+c-1)//c,(b+d-1)//d)

    a = num*c
    b = num*d
print(a+b)