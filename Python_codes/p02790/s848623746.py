a,b = map(int, input().split())
A = a*[b]
B = b*[a]
if a >= b:
   print("".join(map(str, A)))
else:
   print("".join(map(str, B)))