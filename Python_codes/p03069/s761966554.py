n=int(input())
s=input()

black=s.count("#")
white=s.count(".")
b=0
w=0
ans=float('inf')

for i in range(n):
  if s[i]=="#":
    b+=1
  elif s[i]==".":
    w+=1
  
  right_change=white-w
  now=b+right_change
  # print(now)
  ans=min(ans,now)
  
print(min(ans,black,white))
