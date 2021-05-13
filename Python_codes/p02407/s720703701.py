n=input()
l=list(map(int,input().split()))
s=""
for i in l[::-1]:
	s+=str(i)+" "
print(s[:-1])