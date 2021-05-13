n = int(input())
l = list(map(int,input().split()))
left = 0
right = 1
cou = 0
f = 2
while right!=n and right!=n+1:
  if l[left]==l[right]:
    left += 1
    right += 1
  elif l[left]<l[right]:
    while right!=n and l[left]<=l[right]:
      left += 1
      right += 1
    cou += 1
    left +=1
    right += 1
    f = 1
  else:
    while right!=n and l[left]>=l[right]:
      left += 1
      right += 1
    cou += 1
    left += 1
    right += 1
    f = 0
if f==2:
  cou += 1
elif f==1 and l[-2]>l[-1]:
  cou += 1
elif f==0 and l[-2]<l[-1]:
  cou += 1
print(cou)