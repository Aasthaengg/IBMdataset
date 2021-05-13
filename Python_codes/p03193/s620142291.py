n,h,w = map(int,input().split())
c=0
for i in range(n):
    a,b = map(int,input().split())
    if a>=h and b>=w:
        c+=1
print(c)