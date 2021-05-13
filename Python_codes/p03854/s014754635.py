s=input()[::-1]
a=["dreamer"[::-1],"eraser"[::-1],"dream"[::-1],"erase"[::-1]]
st=1
en=0
while st>en:
  st=len(s)
  for m in a:
    
    if s.find(m)==0:
      s=s[len(m):]
    
  en=len(s)
  
print("YES" if s=="" else "NO")