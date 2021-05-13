# -*- coding: utf-8 -*-
import sys
from heapq import heappush, heappop
from bisect import bisect_left, bisect_right

N,Q=map(int, sys.stdin.readline().split())

S=[]
event=[]	#x, s, t
for _ in range(N):
	s,t,x=map(int, sys.stdin.readline().split())
	heappush( event, (x, max(0,s-x) , max(0,t-1-x)) )


D=[ int(sys.stdin.readline().strip()) for _ in range(Q) ]
D.sort()
ans=[ float("inf") for _ in range(Q) ]

Next=[ i+1 for i in range(Q) ]	#Next


while event:
	x,s,t=heappop(event)
	start=bisect_left(D,s)
	end=bisect_right(D,t)

	i=start
	while i<end:
		ans[i]=min(ans[i],x)
		next=Next[i]
		Next[i]=end
		i=next

for x in ans:
	if x==float("inf"):
		print -1
	else:
		print x

