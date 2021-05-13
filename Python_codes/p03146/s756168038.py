s=int(input())
t=[]
k=1
while s not in t:
	t+=[s]
	s=3*s+1 if s%2 else s//2
	k+=1
print(k)