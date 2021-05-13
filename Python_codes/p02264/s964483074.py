#queueを使った方法
from collections import deque

pnum,mtime = map(int,input().split(" "))

q = deque([])
[q.append(input().split(" ")) for u in range(pnum)]

tcnt=0
while len(q) > 0:
	qq = q.popleft()
	ztime = int(qq[1]) - mtime
	if ztime <= 0:
		tcnt += int(qq[1])
		print(qq[0],int(tcnt))
	else:
		q.append([qq[0],ztime])
		tcnt += mtime

