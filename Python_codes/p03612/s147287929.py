n = int(raw_input())
count = 0
res = 0
ais = map(int , raw_input().split())

for i in range(n + 1):
	if (ais[i] if i < n else -1) != i + 1:
		#flush the count
		res += (count + 1)/2# + 1
		count = 0
	else:
		count +=1
print res