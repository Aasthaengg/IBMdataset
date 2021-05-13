n=int(input())
res=[]
for i in range(n):
    s,p=map(str,input().split())
    res.append([s,int(p)])
res1=res
res=sorted(res,key=lambda x:(x[0], -x[1]))
for i in range(n):
	print(res1.index(res[i])+1)