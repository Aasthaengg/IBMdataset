h,w,k = map(int,input().split())
c = []
for a in range(h):
  c.append(list(input()))
res = 0

for i in range(2 ** h):
  for j in range(2 ** w):
    i_s = []
    j_s = []
    for x in range(h):  
      if ((i >> x) & 1): 
        i_s.append(x)  
    for y in range(w):  
      if ((j >> y) & 1): 
        j_s.append(y)  
    b_s = 0
    for i_t in i_s:
      for j_t in j_s:
        if c[i_t][j_t] == "#":
          b_s += 1
    if b_s == k:
      res += 1
print(res)