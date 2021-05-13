S=input()
import collections
counter=collections.Counter(S)

# 後ろと前からxを無視して比較していく
# 同じ文字なら続行、indexで出逢えばOK

ans=0
indf=0
indl=len(S)-1
while indf<indl:
  if S[indf]==S[indl]:
    indf+=1
    indl-=1
    continue
  if S[indf]=="x":
    indf+=1
    ans+=1
  elif S[indl]=="x":
    indl-=1
    ans+=1
  else:
    print(-1)
    break
else:
  print(ans)