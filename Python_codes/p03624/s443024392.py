a = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
b = input()
c = []
d = len(b)

for i in range(int(d)):
  c.append(b[i])

e = list(set(c))
f = sorted(e)
g = len(f)
h = int(0)

if g != 26:
  for i in range(int(g)):
    if f[i] == a[i]:
      h = h + 1
    else:
      print(a[i])
      break
else:
  print("None")
  
if h == g:
  print(a[h])