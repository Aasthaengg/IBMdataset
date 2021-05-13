A,B,T=map(int,input().split())
count=0
condition=A
while condition<=T+0.5 :
  count+=B
  condition+=A
print(count)