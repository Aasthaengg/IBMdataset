h,w,k=map(int,input().split())
s=[list(map(int,list(input()))) for _ in range(h)]
def func(catyoko):
  cattate=0
  past=[0]*10
  for wi in range(w):
    now=[0]*10
    for i in range(1,len(catyoko)):
      for j in range(catyoko[i-1],catyoko[i]):
        now[i-1]+=s[j][wi]
    if max([past[i]+now[i] for i in range(10)])>k:
      if max(now)>k:
        return -10
      else:
        cattate+=1
      past=[nowi for nowi in now]
    else:
      for i in range(10):
        past[i]+=now[i]
  return cattate+len(catyoko)-2

# 横方向の割り方は2^(h-1)通りある。h<=10なので横方向の割り方は全探索する。
# 縦方向の割り方は貪欲法
ans=h+w
for i in range(2**(h-1)):
  catyoko=[0]
  for j in range(h-1):
    if ((i>>j) & 1):#立っているビットのところで処理が走る
      catyoko.append(j+1)
  catyoko.append(h)
  a=func(catyoko)
  #print(a,catyoko)
  if a>=0:
    ans=min(ans,a)
print(ans)
