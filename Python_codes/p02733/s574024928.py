h,w,k=map(int,input().split())
s=[list(map(int,list(input()))) for _ in range(h)]

def func(div):
  ret=0
  n_grp=len(div)
  grp=[0]*n_grp
  div.append(h)
  for c in range(w):
    for r in range(h):
      for i in range(n_grp):
        if div[i]<=r<div[i+1]:
          grp[i]+=s[r][c]
    if max(grp)>k:
      ret+=1
      grp=[0]*n_grp
      for r in range(h):
        for i in range(len(div)):
          if div[i]<=r<div[i+1]:
            grp[i]+=s[r][c]
      if max(grp)>k:
        return -1
  return ret

# 縦の分割の仕方はpow(2,h-1)
ans=h*w
for i in range(pow(2,h-1)):
  div=[0]
  for j in range(h-1):
    if ((i>>j) & 1):#立っているビットのところで処理が走る
      div.append(j+1)
  a=func(div)
  #print(a,div)
  if a>-1:
    ans=min(ans,a+len(div)-2)
print(ans)
