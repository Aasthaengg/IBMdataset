x = [str(e) for e in input().split()]
if(x[1] == '+'):
  ans = int(x[0]) + int(x[2])
else:
  ans = int(x[0]) - int(x[2])
print(ans)