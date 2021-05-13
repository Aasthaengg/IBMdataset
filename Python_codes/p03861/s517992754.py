a,b,x=map(int,input().split())
temp1=(b//x)+1
if 0<=a-1:
  temp2=((a-1)//x)+1
else:
  temp2=0
print(temp1-temp2)
