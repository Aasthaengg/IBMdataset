h,w=map(int,input().split())
a={}
for i in range(26):
  a[chr(i+97)]=0
for i in range(h):
  s=input()
  for j in s:
    a[j]+=1
if h==1 and w==1:print("Yes")
elif h%2==0 and w%2==0:
  for i in a.values():
    if i%4!=0:print("No");exit()
  print("Yes")
elif h%2==1 and w%2==0:
  cnt=0
  for i in a.values():
    if i%4==1 or i%4==3:
      print("No");exit()
    if i%4==2:cnt+=1
  if cnt>w//2:
    print("No")
  else:print("Yes")
elif h%2==0 and w%2==1:
  cnt=0
  for i in a.values():
    if i%4==1 or i%4==3:
      print("No");exit()
    if i%4==2:cnt+=1
  if cnt>h//2:
    print("No")
  else:print("Yes")
else:
  cnt3=0;cnt2=0;cnt1=0
  for i in a.values():
    if i%4==1:cnt1+=1
    elif i%4==2:cnt2+=1
    elif i%4==3:cnt3+=1
  if cnt1+cnt3!=1:print("No")
  elif cnt2+cnt3>(h-1)//2+(w-1)//2:print("No")
  else:
    print("Yes")
