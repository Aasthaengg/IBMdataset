import sys
H,W=map(int,input().split())
S=[]
for i in range(H):
  t=input()
  s=[]
  for j in t:
    if j==".":
      s.append(0)
    else:
      s.append(j)
  S.append(s)
#print(S)
#sys.exit()
for k in range(H):
  for l in range(W):
    if S[k][l]=="#":
      try:
#        sys.stderr.write(str(S[k-1][l-1]))
        S[k-1][l-1]+=1
        if k<=0 or l<=0:
          S[k-1][l-1]-=1
      except:
#        sys.stderr.write("1\n")
        pass
      try:
        S[k-1][l]+=1
        if k<=0:
          S[k-1][l]-=1
      except:
#        sys.stderr.write("2\n")
        pass
      try:
        S[k-1][l+1]+=1
        if k<=0:
          S[k-1][l+1]-=1
      except:
#        sys.stderr.write("3\n")
        pass
      try:
        S[k][l-1]+=1
        if l<=0:
          S[k][l-1]-=1
      except:
#        sys.stderr.write("4\n")
        pass
      try:
        S[k][l+1]+=1
      except:
#        sys.stderr.write("5\n")
        pass
      try:
        S[k+1][l-1]+=1
        if l<=0:
          S[k+1][l-1]-=1
      except:
#        sys.stderr.write("6\n")
        pass
      try:
        S[k+1][l]+=1
      except:
#        sys.stderr.write("7\n")
        pass
      try:
        S[k+1][l+1]+=1
      except:
#        sys.stderr.write("8\n")
        pass
for m in S:
  ans=""
  for n in m:
    ans+=str(n)
  print(ans)
