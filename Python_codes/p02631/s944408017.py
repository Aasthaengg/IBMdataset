n = int(input())
aa = input().split(" ")
a = [int(c) for c in aa]

s = a[0]

for num in a[1:]:
	s ^= num

ans = [0]*n

for i, num in enumerate(a):
	ans[i] = s^num

print(*ans)