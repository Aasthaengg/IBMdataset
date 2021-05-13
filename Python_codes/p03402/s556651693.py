import copy
A,B=map(int,raw_input().split())
h=100
w=100
t=list("#"*(w/2)+"."*(w/2))
l=[ copy.deepcopy(t) for i in range(h)]

A-=1
B-=1

flag=0
# Shiro
if A>0:
	for x in range(1,h,2):
		if flag==1: break
		for y in range(1,w/2-1,2):
			l[x][y]="."
			A-=1
			if A==0:
				flag=1
				break

	
flag=0
# Kuro
if B>0:
	for x in range(1,h,2):
		if flag==1: break
		for y in range(w/2+1,w-1,2):
			l[x][y]="#"
			B-=1
			if B==0:
				flag=1
				break

print "100 100"
for i in l:
	print "".join(i)
	
