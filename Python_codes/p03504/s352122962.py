N,C=map(int,input().split())
f=[[0]*int(1e5) for _ in range(C)]

for i in range(N):
	s,t,c=map(int,input().split())
	f[c-1][s-1:t]=[1]*(t-s+1)

print(max(map(sum,zip(*f))))
