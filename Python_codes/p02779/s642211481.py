n = int(input())
a = set(list(int(i) for i in input().split()))
if n == len(a):
	print("YES")
else:
	print("NO")