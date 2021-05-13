n=int(input())
s=str(input())
t=str(input())
    
cnt=0

if s==t:
  print(n) 
else:
  for i in range(n):
    if s[-i-1:]==t[0:i+1]:
      cnt=i+1
      
  print(n*2-cnt)