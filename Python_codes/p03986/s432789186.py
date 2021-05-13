X = str(input())
X = X.replace("ST","")
lx = len(X)
s_count = 0
t_count = 0
for i in range(lx):
  if X[i] == "S":
    s_count += 1
  else:
    if s_count:
      s_count -= 1
    else:
      t_count += 1
   
print(s_count + t_count)