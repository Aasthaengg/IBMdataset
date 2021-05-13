L,R,d = list(map(int,input().split(' ')))
count = 0
for i in range(R-L+1):
	if (i+L)%d == 0:count += 1
print(count)