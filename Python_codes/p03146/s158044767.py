n=int(input())
l=[]
c=0
while(n not in l):
    if(n%2==0):
        l.append(n)
        n=n//2
    else:
        l.append(n)
        n=3*n+1
    c+=1
print(c+1)
