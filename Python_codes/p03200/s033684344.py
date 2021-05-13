s=str(input())
s=list(s)
count=0
temp=0
for i in range(len(s)):
  if s[i]=="W":
    temp=temp+i-count
    count=count+1
print(temp)