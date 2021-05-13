def div_by_two(x, div_times):
	x = x / 2
	if x == int(x):
		div_times += 1
		div_times = div_by_two(x, div_times)
		
	return div_times
		

N = int(input())

ans = 1
max_div_times = 0
for i in range(1, N+1):
	div_times = div_by_two(i, 0)
	if div_times > max_div_times:
		max_div_times = div_times
		ans = i
		
print(ans)