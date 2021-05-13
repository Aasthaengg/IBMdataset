sx, sy , tx , ty = map(int , input().split())
dx = tx-sx
dy= ty-sy
now = ""
for i in range(0 ,dy):
	now= now+'U'
for i in range(0 , dx):
	now = now+'R'

for i in range(0 , dy):
	now = now+'D'
for i in range(0 , dx):
	now = now+'L'

now = now+'L'
for i in range(0 , dy+1):
	now = now+'U'
for i in range(0 , dx+1):
	now = now+'R'
now = now+'D'

now = now+'R'
for i in range(0 , dy+1):
	now = now+'D'
for i in range(0 , dx+1):
	now = now+'L'
now = now+'U'
print(now)

