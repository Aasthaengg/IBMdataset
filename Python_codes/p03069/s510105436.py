N=int(input())
S=input()
W=[0]*N
B=[0]*N
tmp=0
for i in range(N):
	if S[i]=="#":
		tmp+=1
	B[i]=tmp
tmp=0
for i in range(N):
	if S[i]==".":
		tmp+=1
	W[i]=tmp
Max_W=(max(W))
tmp=float("inf")
for i in range(N-1):
	tmp=min(tmp,B[i]+(Max_W-W[i]))
print(min(tmp,max(B),max(W)))
