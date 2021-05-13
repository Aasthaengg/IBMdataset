n=int(input());a=0
for _ in [0]*n:
  d,s=map(int,input().split())
  a+=s-d+1
print(a)