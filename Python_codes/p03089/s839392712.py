n = int(input())
b = list(map(int,input().split()))
for i in range(n):
	if b[i] > i+1:
		print(-1)
		exit()

ansl = []
while len(b) != 0:
	tmp = 0
	for i in range(len(b)):
		targ = i+1-b[i]
		if targ == 0:
			tmp = i
	ansl.append(str(b[tmp]))
	b.pop(tmp)

ansl.reverse()
print("\n".join(ansl))