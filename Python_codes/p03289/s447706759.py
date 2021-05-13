S = input()
ans = 0

if S[0]=="A":
  S = S[1:]
  if 1<=S.find("C")<=len(S)-2:
    S = S[:S.find("C")]+S[S.find("C")+1:]
    for s in S:
      if 97<=ord(s)<=122:
        ans+=1
    if ans == len(S):
      print("AC")
      exit()
        
print("WA")