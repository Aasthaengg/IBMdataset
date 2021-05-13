#入力:N,M(int:整数)
def input2():
	return map(int,input().split())

#入力:[n1,n2,...nk](int:整数配列)
def input_array():
	return list(map(int,input().split()))

n,k=input2()
p=input_array()
sp=sorted(p)

print(sum(sp[:k]))