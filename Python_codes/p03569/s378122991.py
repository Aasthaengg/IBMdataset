s=input()
left=0
right=len(s)-1
cnt=0
while right-left>0:
  if (s[right]==s[left]):
    right-=1
    left+=1
  elif (s[right]!='x')and(s[left]!='x'):
    print(-1)
    exit()
  elif (s[right]!='x')and(s[left]=='x'):
    left+=1
    cnt+=1
  else:
    right-=1
    cnt+=1
print(cnt)