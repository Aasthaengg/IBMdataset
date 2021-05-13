N = int(input())
masu=[int(x) for x in input().split(" ")]
c=0
for i in range(0,N,2):
	if masu[i]%2 !=0: c += 1
print(c)
