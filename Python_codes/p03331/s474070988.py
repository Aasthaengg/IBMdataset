n=int(input())
s=[]
for i in range(1,n):
  I1=list(map(int,str(i)))
  I2=list(map(int,str(n-i)))
  s.append(int(sum(I1))+int(sum(I2)))
print(min(s))