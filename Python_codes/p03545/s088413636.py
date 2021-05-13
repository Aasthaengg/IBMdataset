x = input()
a=[int(x[0]), int(x[1]), int(x[2]), int(x[3])]
op=['+', '-']
for i in range(2):
  for j in range(2):
    for k in range(2):
      ops = [op[i], op[j], op[k]]
      tmp = a[0]
      for l in range(3):
        if ops[l]=='+':
          tmp = tmp + a[l+1]
        else:
          tmp = tmp - a[l+1]
      if tmp==7:
        break
    if tmp==7:
      break
  if tmp==7:
    break

print(str(a[0])+ops[0]+str(a[1])+ops[1]+str(a[2])+ops[2]+str(a[3])+'=7')
