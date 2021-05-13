n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
sa=sum(a)
sb=sum(b)
if sb<sa:
  print("No")
  exit(0)
husoku_a=0
husoku_b=0
for aa,bb in zip(a,b):
  if bb<aa:
    husoku_a+=aa-bb
  elif bb>aa:
    husoku_b+=(bb-aa)//2

if husoku_a<=husoku_b:
  print("Yes")
else:
  print("No")