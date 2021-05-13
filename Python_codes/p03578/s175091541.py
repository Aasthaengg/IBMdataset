from collections import Counter
n = int(input())
d = list(map(int,input().split()))
c = Counter(d)
m = int(input())
t = list(map(int,input().split()))

for i in t:
	if c[i] == 0:
		print("NO")
		exit()
	else:
		c[i] -= 1

print("YES")