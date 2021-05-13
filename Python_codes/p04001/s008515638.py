s = list(input())
n = (len(s)-1)
sum = 0
pt = []
for i in range(2 ** n):
  tmp = [""] * n
  for j in range(n):
    if (i >> j) &1 :
      tmp[j] = "+"
  pt.append(tmp)
  
for p in pt:
  fr = ""
  for j in range(n):
    
    fr += s[j] + p[j]
  sum += eval(fr+s[n])
    
print(sum)