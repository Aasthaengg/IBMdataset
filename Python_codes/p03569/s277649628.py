s = list(input())
s1=s[::-1]
ans = 0
cnt = 0
cnt1 = 0
while cnt<len(s) and cnt1<len(s) and cnt<=len(s)-1-cnt1:
  if s[cnt]!=s1[cnt1]:
    if s[cnt]=="x" and s1[cnt1]!="x":
      cnt+=1
      ans+=1
    elif s1[cnt1]=="x" and s[cnt]!="x":
      cnt1+=1
      ans+=1
    elif s[cnt]!="x" and s1[cnt1]!="x":
      print(-1)
      exit()
  elif s[cnt]==s1[cnt1]:
    cnt+=1
    cnt1+=1
print(ans)

