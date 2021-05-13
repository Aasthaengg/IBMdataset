n,a,b = map(int,input().split())

d = abs(b-a)
if(d % 2 == 0):
    print(d//2)
else:
    c = min(a-1,n-b)
    c += 1
    d = abs(b-a-1)
    print(c + d // 2)