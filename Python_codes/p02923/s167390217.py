#入力:[n1,n2,...nk](int:整数配列)
def input_array():
	return list(map(int,input().split()))

n=int(input())
H=input_array()

ans=0
tmp_ans=0
for i in range(1,n):
	if H[i-1]>=H[i]:
		tmp_ans+=1
	else:
		if tmp_ans>ans:
			ans=tmp_ans
		tmp_ans=0
if tmp_ans>ans:
	ans=tmp_ans
print(ans)