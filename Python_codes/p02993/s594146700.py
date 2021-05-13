ss=input().strip()
flg=False
for i in range(1,len(ss)):
  if ss[i]==ss[i-1]:
    flg=True
    
if flg==True:
  print("Bad")
else:
  print("Good")