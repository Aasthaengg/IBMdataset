N=int(input())
A,B=map(int,input().split())
P=list(map(int,input().split()))

a=sum(x<=A for x in P)
b=sum(x>A and x<=B for x in P)
c=sum(x>B for x in P)
print(min(a,b,c))