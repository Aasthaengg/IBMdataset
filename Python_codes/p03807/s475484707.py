n = int(input())
A = list(map(int, input().split()))

cnt_even = 0
cnt_odd = 0

for v in A:
	if v % 2 == 0:
		cnt_even += 1
	else:
		cnt_odd += 1

add_even = cnt_odd // 2 # odd + odd = even
cnt_odd -= add_even * 2

print('YES') if cnt_odd == 0 else print('NO')