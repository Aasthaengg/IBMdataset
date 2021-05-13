n=str(input())
s=list(map(str,input().split()))
s=set(s)
if len(s)==4:
  print("Four")
elif len(s)==3:
  print("Three")
elif len(s)==2:
  print("Two")
else:
  print("One")