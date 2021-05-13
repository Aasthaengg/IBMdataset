N=int(input())
D=[int(input()) for _ in range(N)]

se=set([])
for d in D:
	se.add(d)
print(len(se))