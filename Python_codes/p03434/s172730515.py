n=int(input())
a=list(map(int,input().split()))
aa=sorted(a,key=int,reverse=True)
Ali=0
Bob=0
for i in range(n):
	if i%2==0:
	    Ali+=aa[i]
	else:
	    Bob+=aa[i]
print(Ali-Bob)