n=int(input())
a=list(map(int,input().split()))
buka=[0]*n
for i in a:
  buka[i-1]+=1

for b in buka:
  print(b)