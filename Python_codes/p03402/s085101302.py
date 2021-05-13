a,b=map(int,input().split())
a1,a2,b1,b2=(a-1)//49,(a-1)%49,(b-1)//49,(b-1)%49
n=6*(max(a1,b1)+1)
print(n,100)
for i in range(n):
  if i%6==0 or i%6==2:
    print("."+"#"*99)
  elif i%6==3 or i%6==5:
    print("."*99+"#")
  elif i%6==1:
    if i//6<a1:
      print(".#"*50)
    elif i//6==a1:
      print(".#"*(a2+1)+"#"*(100-2*(a2+1)))
    else:
      print("."+"#"*99)
  else:
    if i//6<b1:
      print(".#"*50)
    elif i//6==b1:
      print("."*(100-2*(b2+1))+".#"*(b2+1))
    else:
      print("."*99+"#")
