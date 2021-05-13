n=int(input())
x=[*map(int,input().split())]
s=sorted(x)
l,r=s[n//2-1],s[n//2]
for i in x:
  print([l,r][i<r])