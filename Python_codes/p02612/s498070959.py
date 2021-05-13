N = int(input())

if N % 1000 == 0:
  print("0")
elif N < 1000:
  print(1000-N)
else:
  n = list(str(N))
  print(1000*(1+int(n[0]))-N)