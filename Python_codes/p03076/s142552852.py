import math

dish=[int(input()) for _ in range(5)]
count={str(i%10):[] for i in range(10,-1,-1)}
for t in dish:
	one=t%10
	count[str(one)].append(t)

ans=0
d=0
for k,v in count.items():
	if v!=[]:
		for c in v:
			if d>3:
				ans+=c
			else:
				ans+=math.ceil(c/10)*10
				d+=1
print(int(ans))