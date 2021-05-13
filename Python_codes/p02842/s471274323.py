N = int(input())
for x in range(1,100000):
  if x*108//100==N:
    print(x)
    break
if x==99999:
  print(":(")