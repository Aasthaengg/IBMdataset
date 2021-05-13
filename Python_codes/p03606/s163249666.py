n=int(input())
l=[]
for i in range(n):
    d=list(map(int,input().split()))
    l+=list(range(d[0],d[1]+1))
s=set(l)
print(len(s))
