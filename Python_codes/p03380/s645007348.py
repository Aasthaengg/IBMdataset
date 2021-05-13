n=int(input())
a=list(map(int,input().split()))
p=max(a)
r=p/2
print(p,int(min([i-r for i in a if i!=p],key=abs)+r))