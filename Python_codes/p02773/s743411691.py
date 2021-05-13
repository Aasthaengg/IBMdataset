n=int(input())
a=[]
b=[[] for _ in range(n)]
for i in range(n):
    s=input()
    a.append(s)
a=sorted(a)
d=0
b[0].append(a[0])
for i in range(1,n):
    if a[i]!=a[i-1]:
        d+=1
    b[d].append(a[i])
x=max(len(b[i]) for i in range(n))
for i in range(n):
    if len(b[i])==x:
        print(b[i][0])
    
        
        
    
    
    
    
        
