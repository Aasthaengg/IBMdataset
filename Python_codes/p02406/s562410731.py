#15dpro
n=int(input())
s=''
#print(n)
for i in range(1,n+1):
 #   print(i)
    if i%3==0:
        s+=' '+str(i)
    else:
        x=i
  #      print(x)
        while x>0 and x%10!=3:
      #      print(x)
            x//=10
        if x%10==3:
            s+=' '+str(i)
print(s)