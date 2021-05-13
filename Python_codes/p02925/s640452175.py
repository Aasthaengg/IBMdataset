# -*- coding: utf-8 -*-
import sys
import copy
from collections import defaultdict,deque

N=input()
A=[[]]+[ map(int, sys.stdin.readline().split()) for _ in range(N) ]
C=defaultdict(lambda: 0)

Now=[ 0 for _ in range(N+1)]
game=set()
next_game=set()

for i in range(1,N+1):
	a=i
	b=A[i][0]
	if a>b: a,b=b,a
	game.add((a,b))

day=0

while game:
	next_game=set()
	Visit=defaultdict(lambda: None) 

	for x,y in game:
		now_x=Now[x]
		now_y=Now[y]

		xopp=A[x][now_x]
		yopp=A[y][now_y]

		if (x,y)==(yopp,xopp) and Visit[x] is None and Visit[y] is None:
			Visit[x]=1
			Visit[y]=1
			if now_x<N-2:
				now_x+=1
				Now[x]=now_x
				x_nextopp=A[x][now_x]
				if x_nextopp<x: x,x_nextopp=x_nextopp,x
				next_game.add((x,x_nextopp))

			if now_y<N-2:
				now_y+=1
				Now[y]=now_y
				y_nextopp=A[y][now_y]
				if y_nextopp<y: y,y_nextopp=y_nextopp,y
				next_game.add((y,y_nextopp))

	game=next_game
	day+=1


for i in range(1,N+1):
	if Now[i] != N-2:
		print -1
		quit()
else:
	print day
