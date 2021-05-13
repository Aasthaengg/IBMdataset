n,m=map(int,input().split())
C=set(map(int,input().split()))

ANSLIST=[n]*(n+1)

ANSLIST[0]=0

for i in range(1,n+1):
    ANSLIST[i]=min([ANSLIST[i-c]+1  for c in C if i-c>=0])

print(ANSLIST[n])
