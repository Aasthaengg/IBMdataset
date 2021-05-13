n = int(raw_input())
count = 0
res = 0
ais = map(int , raw_input().split())

for i,a in enumerate(ais):
	
	if a == i +1:
		count += 1
	else:
		#flush the count
		res += (count + 1)/2# + 1
		count = 0

if count: res +=  (count+1)/2 
print res