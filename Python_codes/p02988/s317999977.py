n=int(input())
p=[int(x) for x in input().rstrip().split()]
cnt=0

for i in range(1,n-1):
  l=p[i-1]
  m=p[i]
  r=p[i+1]
  if l<m<r or r<m<l:
    cnt+=1

print(cnt)