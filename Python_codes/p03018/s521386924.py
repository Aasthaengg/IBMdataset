w=input()
count=0
num=len(w)
w1=""
w+=" "
while count<num:
  if w[count]=="A":
    w1+="A"
    count+=1
  elif w[count]=="B":
    if w[count+1]=="C":
      w1+="D"
      count+=2
    else:
      w1+="B"
      count+=1
  else:
    w1+="C"
    count+=1
counta=0
ans=0
num=len(w1)
for i in range(num):
  if w1[i]=="A":
    counta+=1
  elif w1[i]=="D":
    ans+=counta
  else:
    counta=0
print(ans)