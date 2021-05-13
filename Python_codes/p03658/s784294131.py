N,K= map(int, input().split())
l = input().split()
l=[int(s) for s in l]
l.sort()
sum=0
for i in range(K):
	sum+=l[N-i-1]
print(sum)