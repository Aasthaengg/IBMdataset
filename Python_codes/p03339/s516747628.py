N=int(input())
S=input()
#ある場所を決めたときに、右側はすべてW,左側はすべてEになる必要がある
#この変更の数が少なければよい

#最初から最後までのwとeの累積和を計算する
sum_W=[0]*(N+1)
sum_E=[0]*(N+1)
for i in range(N):
	if S[i]=="W":
		sum_W[i+1]+=sum_W[i]+1
	else:
		sum_W[i+1]=sum_W[i]
		
	if S[i]=="E":
		sum_E[i+1]+=sum_E[i]+1
	else:
		sum_E[i+1]=sum_E[i]
ans=N
count=0
for i in range(1,N+1):
	#仮に3番目がリーダーだとすると,左右で動かなければならない人数は
	tmp=sum_W[i-1]+(sum_E[-1]-sum_E[i])
	if tmp<ans:
		ans=tmp
		count=i
print(ans)
#仮に3番目がリーダーだとすると,左右で動かなければならない人数は
#print(sum_W[2],sum_E[5]-sum_E[3])