n,m=map(int,input().split())
d=[]
for i in range(n):
    d.append(int(input()))
print((m-sum(d))//min(d) +len(d))