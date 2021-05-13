n = input()
while True:
  if len(set(list(n))) == 1:
    print(n)
    break
  n = str(int(n)+1)