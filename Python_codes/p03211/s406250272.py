s=list(input())
ans=999
for i in range(0,len(s)-2):
  n=int(s[i]+s[i+1]+s[i+2])
  ab=abs(n-753)
  if ab<ans:
    ans=ab
    
print(ans)