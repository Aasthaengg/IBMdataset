n=input()
n=int(n)
og=n
flag=0
while(n>0):
    d=n%10
    n=n//10
    if(d==9):
        flag=flag+1
        
if(flag>0):
    print("Yes")
else:
    print("No")
    
          
          

    
