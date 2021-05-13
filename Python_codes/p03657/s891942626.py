a, b= map(int, input().split())
x = False
for i in [a, b, a+b]:
  if i%3 == 0:
    x = True
print("Possible" if x else "Impossible")