n=int(input())
a=list(map(int,input().split()))
p=sum(map(abs,a))
print(p-abs(min(a,key=abs))*2 if len([i for i in a if i<0])%2 else p)
