s=input()
b=0
cnt=0
for i in range(len(s)):
  if s[i]=="B":
    b+=1
    cnt+=i
print(int((len(s)*2-b-1)*b*(1/2)-cnt))