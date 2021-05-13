#入力:N,M(int:整数)
def input2():
	return map(int,input().split())

k,x=input2()

st=x-k+1
fi=x+k-1
ans=[]
for i in range(st,fi+1):
	ans.append(i)

print(*ans)