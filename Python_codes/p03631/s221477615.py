n=input()
n=int(n)
og=n
rev=0
while(n>0):
    d=n%10  
    n=n//10
    rev=rev*10+d
if(rev==og):
    print("Yes")
else:
    print("No")
    
        
  


        
