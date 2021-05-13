n = int(input())
l = [int(i) for i in input().split()]

l.sort()
cnt = 0
for i in range(n-1):
	cnt += l[i]
if cnt > l[n-1]:
	print("Yes")
else:
	print("No")
