N=int(input())
K=int(input())
xlis=[int(x) for x in input().split(' ')]
sums=0
for i in range(N):
	ball=xlis[i]
	arob=ball*2
	brob=abs(K-ball)*2
	sums+=min([arob,brob])
print(sums)