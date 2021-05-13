a,b = map(int,input().split())
Flag = "Impossible"
if a%3==0:
  Flag = "Possible"
elif b%3 ==0:
  Flag="Possible"
elif (a+b)%3==0:
  Flag = "Possible"
  
print(Flag)
  
  
