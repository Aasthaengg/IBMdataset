t1, t2 = map(int, input().split())
a1, a2 = map(int, input().split())
b1, b2 = map(int, input().split())
if a1 < b1:
  a1, b1 = b1, a1
  a2, b2 = b2, a2
f = (a1-b1)*t1
l = (b2-a2)*t2
if f > l:
  print(0)
elif f == l:
  print("infinity")
else:
   print(2 * (f//(l-f)) + int(f%(f-l)!=0))