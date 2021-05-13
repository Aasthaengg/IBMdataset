D=int(input())
c=list(map(int,input().split()))
c.insert(0,0)
s=[0]*(D+1)
t=[0]*(D+1)
for i in range(1,D+1):
	s[i]=list(map(int,input().split()))
for i in range(1,D+1):
	t[i]=int(input())

def last(d,i):
	for j in range(d, 0, -1):
		if t[j]==i: return j
	return 0

S=0
for d in range(1, D+1):
	cd = sum((c[i] * (d - last(d, i)) for i in range(1, 27)))
	S += s[d][t[d]-1] - cd
	print(S)