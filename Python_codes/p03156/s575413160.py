import sys

n = int(input())
a, b = map(int, input().split())
p = sorted(list(map(int, input().split())))
cnt_1, cnt_2, cnt_3 = 0,0,0
for i in range(n):
	if p[i] > a:
		break
	cnt_1 += 1

for j in range(i,n):
	if p[j] > b:
		break
	cnt_2 += 1

	if j == n-1:
		print(0)
		sys.exit()

cnt_3 = n-j
print(min(cnt_1,cnt_2,cnt_3))