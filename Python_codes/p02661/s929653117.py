n = int(input())
al=[]
bl=[]
for i in range(n):
    a , b = map(int, input().split())
    al.append(a)
    bl.append(b)
al.sort()
bl.sort()
if n%2==1:
    mi = al[n//2]
    ma = bl[n//2]
    print(int(ma-mi)+1)
else:
    mi = (al[n//2-1]+al[n//2])/2
    ma = (bl[n//2-1]+bl[n//2])/2
    print(int((ma-mi)*2+1))
