S=input()
num=0
ans=0
con=0
upcon=0
before="<"
for s in S:
  if s==before and s=="<":
    upcon+=1
    num+=1
    ans+=num
  if s==">":
    con+=1
    num-=1
    ans+=num
  if s=="<" and before==">":
    ans+=(-num)*(con+(con>upcon))
    con=0
    upcon=1
    num=1
    ans+=num
  before=s
if con!=0:
  ans+=(-num)*(con+(con>upcon))
print(ans)