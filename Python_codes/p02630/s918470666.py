#入力:[n1,n2,...nk](int:整数配列)
def input_array():
	return list(map(int,input().split()))

n=int(input())
a=input_array()
q=int(input())
BC=[input_array() for _ in range(q)]
SUM=sum(a)

A=[0]*(10**5+1)
for i in a:
	A[i]+=1

for bc in BC:
	diff= bc[1]-bc[0]
	SUM+=diff*A[bc[0]]
	A[bc[1]]+=A[bc[0]]
	A[bc[0]]-=A[bc[0]]
	print(SUM)