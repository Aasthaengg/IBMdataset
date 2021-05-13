import sys

a,b,c,d=map(int,input().split())
count=0

if a>=b:
  if a-b<=d:
    count+=1
elif a<b:
  if b-a<=d:
    count+=1
    
if b>=c:
  if b-c<=d:
    count+=1
elif b<c:
  if c-b<=d:
    count+=1
    
if a>=c:
  if a-c<=d:
    print("Yes")
    sys.exit()
elif a<c:
  if c-a<=d:
    print("Yes")
    sys.exit()
    
print("Yes"if count>=2 else "No")