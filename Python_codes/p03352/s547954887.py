X=int(input())
d=[1]
for i in range(2,X+1):
  for j in range(2,X+1):
    t=i**j
    if t>X:
      break
    d.append(t)
print(max(d))