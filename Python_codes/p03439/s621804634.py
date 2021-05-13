n = int(input())
print(0)
even = input()
if even == "Vacant":
  exit()
elif even == "Male":
  odd = "Female"
else:
  odd = "Male"
print(n-1)
d = input()
if d == "Vacant":
  exit()
left = 1
right = n-2
nex = (left+right)//2
while(True):
  print(nex)
  d = input()
  if d == "Vacant":
    exit()
  if (nex%2==0 and d == even) or (nex%2 == 1 and d == odd):
    left = nex + 1
  else:
    right = nex -1
  nex = (left+right)//2