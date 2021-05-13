s=str(input())
ans=0
cnt=0

for i in range(len(s)):
  
  if s[i]=="A" or s[i]== "G" or s[i]== "C" or s[i]== "T":
    cnt=cnt+1
    ans=max(ans, cnt)
    
  else:
    cnt=0
    
print(ans)