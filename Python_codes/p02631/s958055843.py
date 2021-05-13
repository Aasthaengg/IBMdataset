n=int(input())
a=list(map(int,input().split()))
xor=0
for i in a:
	xor^=i
b=[]
for i in a:
	b.append(xor^i)
print(*b)
