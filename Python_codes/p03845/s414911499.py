n=int(input())
t=list(map(int,input().split()))
m=int(input())
t_tot=sum(t)
p=x=0
a=0

for _ in range(m):
	p,x=map(int,input().split())
	a=t_tot-t[p-1]+x
	print(a)