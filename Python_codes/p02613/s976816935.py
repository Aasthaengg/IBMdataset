n=int(input())
count1=0
count2=0
count3=0
count4=0
 
for i in range(n):
  s=input()
  if(s=="AC"):
    count1+=1
  elif(s=="WA"):
    count2+=1
  elif(s=="TLE"):
    count3+=1
  elif(s=="RE"):
    count4+=1
print("AC x",count1)
print("WA x",count2)
print("TLE x",count3)
print("RE x",count4)