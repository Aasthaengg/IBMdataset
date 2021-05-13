a,b,c = map(int, input().split())
k = int(input())
s = 0

while(a>=b):
  b *= 2
  s += 1
while(b>=c):
  c *= 2
  s += 1
  
if(s<=k):
  print("Yes")
else:
  print("No")
