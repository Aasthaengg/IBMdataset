N = int(input())
A = list(map(int, input().split()))
def xored(a, b):
  y = 0
  base = 1
  while a != 0 or b != 0:
    y += ((a + b) % 2) * base
    base *= 2
    a //= 2
    b //= 2
  return y

if max(A) == 0:
  print("Yes")
else:
  if N % 3 != 0:
    print("No")
  else:
    D = {}
    for i in A:
      if i in D:
        D[i] += 1
      else:
        D[i] = 1
    if len(D) > 3:
      print("No")
    else:
      if len(D) == 3 and min(D[i] for i in D) == max(D[i] for i in D):
        L = [i for i in D]
        if xored(L[0], L[1]) == L[2]:
          print("Yes")
        else:
          print("No")
      elif len(D) == 2:
        if 0 not in D:
          print("No")
        else:
          if D[0] >= N // 3:
            print("Yes")
          else:
            print("No")
      else:
        print("No")