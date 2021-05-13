s,c,sa=input(),0,False
while c<len(s):
  if c>0 and s[c-1]==s[c]:
    sa=True
  c+=1
print("Bad" if sa else "Good")