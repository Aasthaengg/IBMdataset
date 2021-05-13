s = str(input())
L = [753]
for i in range(len(s) - 2):
  a = int(s[i:i + 3])
  L.append(a)
L.sort()
for j in range(len(L)):
  if L[j] == 753:
    if j == len(L) - 1:
      print(L[j] - L[j - 1])
      break
    if j == 0:
      print(L[j + 1] - L[j])
      break
    else:
      if L[j + 1] - L[j] <= L[j] - L[j - 1]:
        print(L[j + 1] - L[j])
      else:
        print(L[j] - L[j - 1])
      break