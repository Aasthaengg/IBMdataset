S = input()
count=0
if S[0]=="A":
  for i in range(2,max([len(S)-1,3]),1):
    if S[i]=="C":
      count+=1
      idx=i
  if count==1:
    s=S[1:idx]+S[idx+1:]
    if s==s.lower():
      print("AC")
    else:
      print("WA")
  else:
    print("WA")
else:
  print("WA")