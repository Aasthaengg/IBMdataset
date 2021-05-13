c=int(input())
n=0
m=0
for i in range(c):
    a,b=map(str,input().split())
    if a>b:
        n+=3
    elif a<b:
        m+=3
    else:
        n+=1
        m+=1
print(n,m)    
