# -*- coding: utf-8 -*-
import sys
from collections import defaultdict,deque

N=input()
M=[[None]]

for i in range(N):
	A=map(int, sys.stdin.readline().split())
	M.append(A)

position=[0]*(N+1)

ans=0
goal_cnt=0
day=0
q=deque()

game=set()
for me in range(1,N+1):
	p=position[me]
	opp=M[me][p]	#Opponent
	if me>opp: me,opp=opp,me
	game.add((me,opp))


while game:
	Visit=defaultdict(lambda: None) 
	next_game=set()
	for me,opp in game:
		opp_of_me=M[me][position[me]]
		opp_of_opp=M[opp][position[opp]]
		if me==opp_of_opp and opp==opp_of_me and Visit[me] is None and Visit[opp] is None:
			Visit[me]=1
			Visit[opp]=1
			position[me]+=1
			position[opp]+=1
			try:
				next_opp_of_me=M[me][position[me]]
				if me>next_opp_of_me: me,next_opp_of_me=next_opp_of_me,me
				next_game.add((me,next_opp_of_me))
			except:
				goal_cnt+=1
			try:
				next_opp_of_opp=M[opp][position[opp]]
				if opp>next_opp_of_opp: opp,next_opp_of_opp=next_opp_of_opp,opp
				next_game.add((opp,next_opp_of_opp))
			except:
				goal_cnt+=1
	day+=1
	game=next_game

if goal_cnt!=N:
	print -1
else:
	print day