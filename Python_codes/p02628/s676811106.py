N,K = map(int,input().split())
list = list(map(int,input().split()))

list.sort()

total=0
for i in range(K):
	total+=list[i]
print(total)