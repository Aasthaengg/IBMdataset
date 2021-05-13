T=input()
while True:
  if T==str():
    print("YES")
    exit()
  if len(T)<5:
    print("NO")
    exit()
  if T[-5:]=="dream":
    T=str(T[:-5])
  elif T[-7:]=="dreamer":
    T=str(T[:-7])
  elif T[-5:]=="erase":
    T=str(T[:-5])
  elif T[-6:]=="eraser" :
    T=str(T[:-6])
  else:
    print("NO")
    exit()