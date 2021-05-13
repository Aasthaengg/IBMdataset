#入力:N,M(int:整数)
def input2():
	return map(int,input().split())
  
n,k,q=input2()
A=[int(input()) for _ in range(q)]

P=[0]*n


for a in A:
	P[a-1]+=1

for p in P:
	if p >q-k:
		print("Yes")
	else:
		print("No")