c=0
n=int(input())
s=input().split()
q=int(input())
t=input().split()
for i in t:
	for j in s:
		if int(i)==int(j):
			c +=1
			break
print(c)
