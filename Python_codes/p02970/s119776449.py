n,d = map(int,input().split())
c = d*2+1
if n%c ==0:
    print(int(n//c))
else:
    print(int(n//c)+1)