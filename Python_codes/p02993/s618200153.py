S=input()
pre = S[0]
for s in S[1:]:
  if pre == s:
    print("Bad"); exit()
   
  pre = s
  
print("Good")