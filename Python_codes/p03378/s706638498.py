N,M,X=map(int,input().split())
p=n=0
for i in list(map(int,input().split())):
    if i>X:
        p+=1
    else:
        n+=1
print(min(p,n))
