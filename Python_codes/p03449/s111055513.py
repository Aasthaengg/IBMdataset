n=int(input())
a1=list(map(int,input().split()))
a2=list(map(int,input().split()))
cand=0
cand_max=0

for i in range(n):
	cand += sum(a1[:(i+1)])+sum(a2[i:n])
	if cand > cand_max:
		cand_max=cand
	cand=0

print(cand_max)