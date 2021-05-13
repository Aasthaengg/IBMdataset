#入力:[n1,n2,...nk](int:整数配列)
def input_array():
	return list(map(int,input().split()))
  
n,m=map(int,input().split())
k=[]
s=[]
for _ in range(m):
	tmp=input_array()
	k.append(tmp[0])
	s.append(tmp[1:])
p=input_array()
ans=0
for i in range(2**n):
	tmp=[]
	ans_tmp=0
	for j in range(n):
		tmp.append(i>>j&1)
	for c in range(m): # スイッチのチェック
		sw=s[c]
		sum_sw=0
		for l in sw:
			if tmp[l-1]==1:
				sum_sw+=1
		if sum_sw%2==p[c]:
			ans_tmp+=1
	if ans_tmp==m:
		ans+=1

print(ans)