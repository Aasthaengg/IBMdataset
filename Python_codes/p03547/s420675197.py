x = {'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15}
a,b = map(str, input().split())
if x[a] > x[b]:
  print(">")
elif x[a] < x[b]:
  print("<")
elif x[a] == x[b]:
  print("=")