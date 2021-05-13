o = input()
e = input()
res = ""
if len(o)>len(e):
  for i in range(len(e)):
    res = res + o[i]
    res = res + e[i]
  res = res + o[len(o)-1]
else:
  for i in range(len(e)):
    res= res + o[i]
    res= res + e[i]
print(res)
