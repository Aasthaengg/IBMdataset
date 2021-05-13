from itertools import accumulate
n,c=map(int,input().split())
time=[0]*(10**5+2)
stc=[]
for i in range(n):
	s,t,c=map(int,input().split())
	stc.append([s,t,c])
stc.sort(key=lambda x:(x[2],x[0]))
for i in range(n-1):
	if stc[i][2]==stc[i+1][2]:
		if stc[i][1]==stc[i+1][0]:
			stc[i+1][0]=stc[i][0]
			stc[i]=[-1]
lis=[]
for i in range(n):
	if stc[i]!=[-1]:
		lis.append(stc[i])
for i in range(len(lis)):
	time[lis[i][0]-1]+=1
	time[lis[i][1]]-=1
print(max(accumulate(time)))