
L = ["A","B","C","D","E","F"]
P,Q = input().split()
p = L.index(P)
q = L.index(Q)
if p>q:
  print(">")
elif p<q:
  print("<")
else:
  print("=")