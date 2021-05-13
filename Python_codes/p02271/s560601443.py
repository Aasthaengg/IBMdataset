n = int(raw_input())
a = map(int, raw_input().split())
q = int(raw_input())
m = map(int, raw_input().split())

add_result = [0]*2001
for i in a:
	for j in range(2000, -1, -1):
		if add_result[j] == 1:
			add_result[i+j] = 1
			#print(i, j, i+j)	
	add_result[i] = 1
	#print i

for target in m:
	if add_result[target] == 1:
		print("yes")
	else:
		print("no")