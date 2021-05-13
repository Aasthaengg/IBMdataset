n = int(input())
tsk = []
for i in range(n):
	a,b = map(int,input().split())
	tsk.append([a,b])

tsk.sort(key = lambda x:x[1])

t = 0
ans = 'Yes'

for i in range(n):
	l = tsk[i]
	t += l[0]
	if t > l[1]:
		ans = 'No'
		break
print(ans)