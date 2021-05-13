N=input()
input = [int(input()) for i in range(int(N))]
maxv=-10000000000
minv=10000000000
for i,x in enumerate(input):
	maxv = max(maxv, input[i]-minv)
	minv = min(minv, input[i])
print(maxv)