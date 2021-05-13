n,y = map(int,input().split())
c = (y%5000)//1000
y -= c*1000
n -= c
for i in range(100000):
    a = (y-5000*n)//5000
    b = n - a
    if 0 <= a and 0 <= b and 0 <= c:
        print(a,b,c)
        break
    c += 5
    n -= 5
    y -= 5000
    
    if i == 100000 - 1:
        print(-1,-1,-1)
