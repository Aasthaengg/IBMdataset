N=int(input())
a=list(map(int, input().split()))
count=0
cur=1
for x in a:
  if x==cur:
    count+=1
    cur+=1
print(N-count if count!=0 else -1)
