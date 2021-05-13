a,b,c= map(int,input().split())
cnt = 0
if a == b and b == c:
    if a%2 == 0 and b%2 == 0 and c%2 == 0:
        print(-1)
        exit()
    else:
        print(0)
        exit()
while a%2 == 0 and b%2 == 0 and c%2 == 0:
    cnt +=1
    x =(b+c)//2
    y =(c+a)//2
    z =(b+a)//2
    a = x
    b = y
    c = z
print(cnt)