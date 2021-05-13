import collections
n=int(input())
v=list(map(int,input().split()))
v1=v[0::2]
v2=v[1::2]
c1=collections.Counter(v1).most_common()
c2=collections.Counter(v2).most_common()
if c1[0][0] != c2[0][0]:
	if len(c1) == 1 and len(c2) == 1:
		print(0)
		exit()
	elif len(c1) == 1:
		print(n//2-c2[0][1])
		exit()
	elif len(c2) == 1:
		print(n//2-c1[0][1])
		exit()
	else:
		print(n-c1[0][1]-c2[0][1])
		exit()
else:
	#最頻値が同じ
	if len(c1) == 1 and len(c2) == 1:
		print(n//2)
		exit()
	elif len(c1) == 1:
		print(n//2-c2[1][1])
		exit()
	elif len(c2) == 1:
		print(n//2-c1[1][1])
		exit()
	else:
		print(min(n-c1[1][1]-c2[0][1],n-c1[0][1]-c2[1][1]))
		exit()