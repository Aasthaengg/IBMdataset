S=input()
S=S.replace("BC","X")
# "X"の移動先
target=0
ans=0
for i in range(len(S)):
  if S[i]=="X":
    ans+=(i-target)
    target+=1
  elif S[i]!="A" and S[i]!="X":
    # A,X以外の文字より左には移動できないので、その右位置が移動可能な左端となる。
    target=i+1
print(ans)
