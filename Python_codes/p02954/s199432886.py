s=str(input())
s=list(s)
ans=[0]*len(s)
t=0
r=0
l=0
for i in range(len(s)-1):
  if s[i]=="L" and s[i+1]=="R":
    for j in range(t,i+1):
      if s[j]=="R" and s[j+1]=="L":
        if (i+1-t)%2==0:
          ans[j]=ans[j]+(i+1-t)//2
          ans[j+1]=ans[j+1]+(i+1-t)//2
        else:
          if t%2==j%2:
            ans[j]=ans[j]+(i+1-t)//2+1
            ans[j+1]=ans[j+1]+(i+1-t)//2
          else:
            ans[j+1]=ans[j+1]+(i+1-t)//2+1
            ans[j]=ans[j]+(i+1-t)//2
        t=i+1
        break
for j in range(t,len(s)):
  if s[j]=="R" and s[j+1]=="L":
    if (len(s)-t)%2==0:
      ans[j]=ans[j]+(len(s)-t)//2
      ans[j+1]=ans[j+1]+(len(s)-t)//2
    else:
      if t%2==j%2:
        ans[j]=ans[j]+(len(s)-t)//2+1
        ans[j+1]=ans[j+1]+(len(s)-t)//2
      else:
        ans[j+1]=ans[j+1]+(len(s)-t)//2+1
        ans[j]=ans[j]+(len(s)-t)//2
print(" ".join(map(str,ans)))