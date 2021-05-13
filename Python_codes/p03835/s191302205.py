K,S = map(int,input().split())
if S == 0:
  print(1)
  exit()
z = 0
o = 0
t = 0
start = min(S,K)
for i in reversed(range(start+1)):
  if i < (S-1)//3 + 1:
    break
  else:
    num = min(S-i,i)-(S-i+1)//2 + 1
    z += num
    if num == 1:
      if (S-i) % 2 == 0 or min(S-i,i) == i:
        z -= 1
        o += 1
    else:
      if (S-i) % 2 == 0:
        z -= 1
        o += 1
      if min(S-i,i) == i:
        z -= 1
        o += 1
        
      
if S % 3 == 0:
  t += 1
  o -= 1
print(z*6 + o*3 + t)