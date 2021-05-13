t = 1
# t = input()
# t = int(t)
def max(a,b):
	if a > b:
		return a
	return b
while t > 0:
	t -= 1
	n = int(input())
	# n,k = map(int,input().strip().split())
	v = list(map(int,input().strip().split()))[0:n]
	# m = {}
	l = []
	for i in range(n):
		l.append(0)
	# ans = 0
	j = 1
	for i in v:
		l[i-1] = j
		j += 1
	# print(ans)
	for i in l:
		print(i,end=" ")
