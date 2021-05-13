n=int(input())
cnt=0
p=[int(x) for x in input().rstrip().split()]
for i in range(1,n-1):
  if p[i-1]<p[i]<p[i+1] or p[i+1]<p[i]<p[i-1]:
    cnt+=1
print(cnt) 