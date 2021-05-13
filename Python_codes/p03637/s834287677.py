n=int(input())
a=list(map(int,input().split()))
cnt_odd=0
cnt_even=0
cnt_4=0
for i in range(n):
  if a[i]%2!=0:
    cnt_odd+=1
  else:
    cnt_even+=1
    if a[i]%4==0:
      cnt_4+=1
if cnt_even-cnt_4==0:
  if cnt_4+1>=cnt_odd:
    print("Yes")
  else:
    print("No")
else:
  if cnt_4>=cnt_odd:
    print("Yes")
  else:
    print("No")