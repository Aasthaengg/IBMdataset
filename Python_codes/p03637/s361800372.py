n = int(input())
a_list = list(map(int, input().split()))
counts = [0] * 3
for a in a_list:
	if a%4 == 0:
		counts[0] += 1 		 
	elif a%2 == 0:
		counts[1] += 1
	else:
		counts[2] += 1
r = 'Yes' if counts[2] <= counts[0]+1 else 'No'
if r == 'Yes':
	two_v = counts[1]
	four_v = counts[0] - counts[2]
	mod = two_v%2	
	if mod == 0 or mod - four_v < 2:
		r = 'Yes'
	else:
		r = 'No'
print(r)