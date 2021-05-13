import sys
n=int(input())
b=True
print(0)
w1=input()
if w1=="Vacant":
  b=False
  sys.exit()
print(n-1)
w2=input()
if w2=="Vacant":
  b=False
  sys.exit()
left=0
right=n-1
count=2
while b and count<20:
  mid=(left+right)//2
  print(mid)
  w=input()
  count+=1
  if w=="Vacant":
    b=False
    sys.exit()
  else:#left%2 right%2 mid%2 が等しいかどうか全部で4通り
    if left%2==mid%2 and w1!=w:
      right=mid
      w2=w
    elif left%2!=mid%2 and w1==w:
      right=mid
      w2=w
    elif right%2==mid%2 and w2!=w:
      left=mid
      w1=w
    elif right%2!=mid%2 and w2==w:
      left=mid
      w1=w