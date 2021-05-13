N=int(input())
ans=""
if N==0:
  ans="0"
while N!=0:
  if N%2!=0:
    ans+="1"
  else:
    ans+="0"
  N=-(N//2)
print(ans[::-1])
