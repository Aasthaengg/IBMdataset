S = str(input())
alp = "abcdefghijklmnopqrstuvwxyz"
s = len(S)
for i in range(s):
  alp = alp.replace(S[i],'')
if alp != '':
  print(S+alp[0])
  exit()
else:
  if S == "zyxwvutsrqponmlkjihgfedcba":
    S = "-1"
  else:
    for j in range(s-1,0,-1):
      if S[j] > S[j-1]:
        alp = list(S[j-1:])
        alp = sorted(alp)
        for k in range(len(alp)+1):
          if alp[k] == S[j-1]:
            S = S[:j-1]+alp[k+1]
            print(S)
            exit()
print(S)