s=int(input())
m=10
ans=0
for i in range(0,4):
  n=s%10
  if m==n:
    print("Bad")
    ans+=1
    break;
  m=n
  s//=10
if ans==0:
  print("Good")