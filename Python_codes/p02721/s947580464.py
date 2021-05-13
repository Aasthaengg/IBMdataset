#coding:utf-8
import sys
N,K,C=map(int,input().split())
S=input()
S_R=S[::-1]
L=[]
R=[]
loop=0
cnt=0
while (loop<N):
	if S[loop]=="o":
		L.append(loop+1)
		cnt+=1
		loop+=C+1
	else:
		loop+=1
	if cnt>K:
		break
if cnt<K:
	exit()
loop=0
cnt=0

while (loop<N):
	if S_R[loop]=="o":
		R.append(N-loop)
		cnt+=1
		loop+=C+1
	else:
		loop+=1
	if cnt>K:
		break
if cnt<K:
	exit()

R=R[::-1]
for i in range(K):
	if L[i]==R[i]:
		print(L[i])