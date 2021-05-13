import sys
N=input()
#print N
a=[]
a=map(int,raw_input().split())
#print a

if max(a)==min(a):
	print 0
	sys.exit()
elif abs(max(a))>abs(min(a)):
	num=(max(a),a.index(max(a)))
else:
	num=(min(a),a.index(min(a)))
#print num

ans=[]
for i in range(N):
	a[i]+=num[0]
	ans.append((num[1]+1,i+1))

if num[0]>=0:
	for i in range(N-1):
		ans.append((i+1,i+2))
else:
	for i in range(N,1,-1):
		ans.append((i,i-1))

print len(ans)
for i,j in ans:
	print i,j