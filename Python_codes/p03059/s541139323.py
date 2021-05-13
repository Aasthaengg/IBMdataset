a,b,t=map(int,input().split())
cnt=0
c=a
while a<=t :
  cnt+=b
  a+=c

print(cnt)