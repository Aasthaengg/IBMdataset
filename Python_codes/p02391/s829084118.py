a,b = input().split()
a = int(a)
b = int(b)
c = ''
if a > b:
   c = '>'
elif  a < b:
   c = '<'
else:
  c = '=='
print("a %s b"%(c))