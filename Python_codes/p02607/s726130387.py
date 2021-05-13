n=int(input())
c=list(map(int,input().split()))
count=0
for i in range(len(c)):
  count+=((i+1)*(c[i]))&1
print(count)
