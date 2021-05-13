a = list(input())
b = list(input())
c = list(input())
cur = "a"
while(True):
  if cur == "a":
    if not a:
      print("A")
      break
    cur = a.pop(0)
  if cur == "b":
    if not b:
      print("B")
      break
    cur = b.pop(0)
  if cur == "c":
    if not c:
      print("C")
      break
    cur = c.pop(0)