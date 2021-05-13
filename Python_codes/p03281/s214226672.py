import collections
n = int(raw_input())
count = 0
cc= collections.Counter()
for i in range(1,n + 1):
	j = i
	while(j <= n):
		cc[j] += 1
		j +=i
	if i % 2 and cc[i] == 8 :
		count +=1
print count