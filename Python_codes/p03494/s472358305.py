n=int(input())
a= list(map(int, input().strip().split()))
def how_many_times_divisible(n):
	ans = 0
	while n % 2 == 0:
		n /= 2
		ans += 1
	return ans
ans = min(map(how_many_times_divisible, a))
print(ans)
