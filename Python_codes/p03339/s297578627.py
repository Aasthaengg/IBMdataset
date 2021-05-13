n=int(input())
s=input()
e=s.count("E")
w=n-e
cnt_e=0
cnt_w=0
maxi=0
for i in range(n):
  if s[i]=="E":
    if maxi<=(w-cnt_w)+cnt_e:
      maxi=(w-cnt_w)+cnt_e
    cnt_e+=1
  else:
    if maxi<=(w-cnt_w-1)+cnt_e:
      maxi=(w-cnt_w-1)+cnt_e
    cnt_w+=1
print(n-(maxi+1))