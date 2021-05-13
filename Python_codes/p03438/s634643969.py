n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
s = 0
t = 0
for i in range(n):
	k = b[i] - a[i]
	if k < 0:
		s += -k
	elif k > 0:
		t += k//2
if s <= t:
	print("Yes")
else:
	print("No")