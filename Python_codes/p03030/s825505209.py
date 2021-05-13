n=int(input())
sp=[]
for i in range(n):
	s,p=input().split()
	sp.append([s,int(p),i+1])

sort_sp=sorted(sp,key=lambda x:(x[0],-x[1]))

for ans in sort_sp:
	print(ans[2])