N = int(input())
MM = input()
x = 0
maxi = 0
for i in MM:
  if i =='D':
    x -=1
  else:
    x +=1
    if x > maxi:
      maxi = x
print(maxi)