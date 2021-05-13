from collections import Counter
H, W = map(int,input().split())
A = ""
for _ in range(H):
  A += input()

cA = Counter(A)

if H % 2 == 1 and W % 2 == 1:
  one = 1
  two = H // 2 + W // 2
  four = (H // 2) * (W // 2)
else:
  one = 0
  two = (H * (W % 2) + W * (H % 2)) // 2
  four = (H // 2) * (W // 2)

# print(one, two, four)

vals =[val for val in cA.values()]

# print(vals)

# one
while one > 0:
  for i in range(len(vals)):
    _, m = divmod(vals[i], 4)
    if m == 1 or m == 3:
      vals[i] -= 1
      break # 
  one -= 1

# print(vals)    

# two
if two > 0:
  for i in range(len(vals)):
    _, m = divmod(vals[i], 4)
    if two > 0 and m == 2:
      vals[i] -= 2
      two -= 1
          
# print(vals)

# four
while four > 0:
  for i in range(len(vals)):
    _, m = divmod(vals[i], 4)
    if vals[i] != 0 and m == 0:
      vals[i] -= 4
      break
  four -= 1

# print(vals)      
# print(one, two, four)

# two
while two > 0:
  for i in range(len(vals)):
    _, m = divmod(vals[i], 2)
    if vals[i] != 0 and m == 0:
      vals[i] -= 2
      break
  two -= 1

# print(vals)      
# print(one, two, four)
  
if all([val == 0 for val in vals]):
  print("Yes")
else:
  print("No")