s=int(input())
seq = [s]
cou = 1
while True:
  cou += 1
  if s%2==0:
    new = s/2
  else:
    new = 3*s+1
  if new in seq: break
  else:
    seq.append(new)
    s = new
print(cou)