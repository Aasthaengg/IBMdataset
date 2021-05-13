s=input()

left=0
right=len(s)-1

ans=0
while left<right:
  c1=s[left]
  c2=s[right]
  if c1==c2:
    left+=1
    right-=1
    continue

  elif c1!='x' and c2!='x':
    print(-1)
    exit()
  elif c1=='x':
    ans+=1
    left+=1
  elif c2=='x':
    ans+=1
    right-=1

print(ans)