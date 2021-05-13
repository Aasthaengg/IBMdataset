a,b=map(str,input().split())
List = ["A","B","C","D","E","F"]
if a == b:
  print("=")
c = 0
d = 0
for i in range(6):
  if a == List[i]:
    c = i
  if b == List[i]:
    d = i
if c < d:
  print("<")
elif d < c:
  print(">")