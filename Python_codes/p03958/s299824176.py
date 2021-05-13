k,t=map(int,input().split())
a=list(map(int,input().split()))
aa=max(a)
b=sum(a)
c=b-aa
print(max(aa-1-c,0))