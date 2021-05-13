D = int(input())
c = list(map(int,input().split()))
s = [list(map(int,input().split())) for i in range(D)]
t = [int(input()) for i in range(D)]
tmp = 0
last = [0]*(26)
v = [0]*(D+1) #満足度これだけi=日付他のはi-1=日付


for i in range(D):
	tmp = 0
	tmp += v[i] + s[i][(t[i]-1)]
	last[t[i]-1] = (i+1)
	for j in range(26):
		tmp -= c[j] * (i+1 - last[j]) 
	v[i+1]=tmp
#print(v)
for i in range(1,D+1):
	print(v[i])