S=str(input())
S2=[]
ans=0
for i in range(len(S)):
  for j in range(len(S)+1):
    S2=S[i:j]
    que=len(S2)
    S2=S2.replace("A","")
    S2=S2.replace("G","")
    S2=S2.replace("C","")
    S2=S2.replace("T","")
    if S2=="":
      if que>ans:
        ans=que
    S2=[] 
print(ans)