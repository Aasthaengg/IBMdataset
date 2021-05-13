n=input()
out=''
for i in range(len(n)):
  if n[i]=='9':out += '1'
  else: out += '9'
print(out)