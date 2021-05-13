a,b,c =map(int, raw_input().split())
n=0
for i in range(b-a+1):
 if(c%(a+i)==0):
  n=n+1
print n