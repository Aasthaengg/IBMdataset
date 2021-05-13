N,M,Q=map(int, input().split())

a_ls=[]
b_ls=[]
c_ls=[]
d_ls=[]

for vnwrjvnwakn in range(Q):
	abcd=list(map(int, input().split()))
	a_ls+=[abcd[0]]
	b_ls+=[abcd[1]]
	c_ls+=[abcd[2]]
	d_ls+=[abcd[3]]



import itertools
As=itertools.combinations_with_replacement(range(1,M+1),N)
ans=0
for A in As:
	score=0
	Als=list(A)
	for i in range(Q):
		if Als[b_ls[i]-1]-Als[a_ls[i]-1]==c_ls[i]:
			score+=d_ls[i]
	
	ans=max(ans,score)


print(ans)
