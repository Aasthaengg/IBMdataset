n=int(input())
a=[]
for i in range(n):
    a.append(int(input()))
m=max(a)
b=sorted(a)
m2=b[-2]
for i in range(n):
    if a[i]==m:
        print(m2)
    else:
        print(m)
            
    
