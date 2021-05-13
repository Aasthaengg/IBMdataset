n,c=map(int,input().split())
t=[[0]*10**5 for i in range(c)]
for i in range(n):
	a,b,c=map(int,input().split())
	t[c-1][a-1:b]=[1]*(b-a+1)
print(max(map(sum,zip(*t))))