n = int(raw_input())
i = 1
print "",

while i <= n:
  if i%3 == 0:
      print i,
  else:
      I = str(i)
      for j in range(len(I)):
          if I[j] == '3':
              print I,
              break
  i += 1