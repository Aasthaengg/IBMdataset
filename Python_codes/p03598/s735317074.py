N=int(input())
K=int(input())
l = input().split()
l=[int(s) for s in l]
sum=0

for i in range(N):
	sum+=min(l[i]*2,abs(K-l[i])*2)
print(sum)