n, a, b = map(int, input().split())
if a>b:
  if (a-b)%2==0:
    print("Alice")
  else:
    print("Borys")
elif a<b:
  if (b-a)%2==0:
    print("Alice")
  else:
    print("Borys") 