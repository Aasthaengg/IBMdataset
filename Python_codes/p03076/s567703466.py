sum=0
max=0
for i in range(5):
  A=int(input())
  s=((A+9)//10)*10
  #print(s)
  p=abs(A-s)%10
  if p>max:
    max=p
    #print(max)
  sum+=s
print(sum-max)