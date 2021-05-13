n=int(input())
res=0
a1=int(input())
if a1!=0:
  print(-1)
  exit()
try:a2=int(input())
except:
      print("0")
      exit()
for  i in range(n-2):
  if a2-a1>1:
    print("-1")
    exit()
  if a2<=a1:
    res+=a1
  a1=a2
  a2=int(input()) 
if a2-a1>1:
    print("-1")
    exit()
if a2<=a1:
    res+=a1
res+=a2
print(res)