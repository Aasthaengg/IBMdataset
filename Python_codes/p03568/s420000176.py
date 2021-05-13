N=int(input())
L=list(map(int,input().split()))
ans=3**N
tmp=1
for i in L:
	if i%2==1:
		tmp=tmp*1
	else:
		tmp=tmp*2
print(ans-tmp)