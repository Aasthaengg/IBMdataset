import queue
h,w=map(int,input().split())
INF=10**9
s=[[-1]* w for _ in range(h)]
b=0
for i in range(h):
	x=input()
	for j in range(w):
		if x[j]==".":
			s[i][j] = INF
		else:
			b+=1

q=queue.Queue()
s[0][0]=0
q.put((0,0))

def test(x,y,t):
	if 0<=x<h and 0<=y<w:
		u=s[x][y]
		if t<u:
			s[x][y]=t
			q.put((x,y))

while not q.empty():
	x,y=q.get()
	t=s[x][y]
	test(x+1,y,t+1)
	test(x-1,y,t+1)
	test(x,y+1,t+1)
	test(x,y-1,t+1)

x=s[h-1][w-1]
print(-1 if x==INF else h*w-b-x-1)