a,b = map(int,input().split())
if a > b:
    tmp = b
    b = a
    a = tmp
for i in range(1,b+1):
    if (i*a)%b == 0:
        break
print(a*i)
