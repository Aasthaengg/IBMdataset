import math

n = int(input())


def ts(x):
    return x * (x + 1)


m = n
for i in range(math.ceil(math.sqrt(2 * n) - 2), math.floor(math.sqrt(2 * n)) + 1, 1):
    if ts(i) < 2 * n <= ts(i + 1):
        m = i + 1
        break



if m % 2 == 0:
    a = n % (m + 1)
    b = n // (m + 1)
    if a != 0:
        print(a)
    i = 1
    c = 0
    while c != b:
        if i != a and m + 1 - i != a:
            print(i)
            print(m + 1 - i)
            c += 1
        i += 1
else:
    """
  check=[]
  if a!=0:
      check.append(a)
  i = 1
  c = 0
  while c!=b and i<(m+1)//2:
      if i!=a and m+1-i!=a:
          check.append(i)
          check.append(m+1-i)
          c+=1
      i+=1
  if c==b:
      for i in check:
          print(i)
  else:

      n-=(m+1)//2
      a = n % (m + 1)
      b = n // (m + 1)
      if m % 2 == 0:
          if a != 0:
              print(a)
          i = 1
          c = 0
          while c != b:
              if i != a and m + 1 - i != a:
                  print(i)
                  print(m + 1 - i)
                  c += 1
      """
    print(m)
    n -= m
    m -= 1

    a = n % (m + 1)
    b = n // (m + 1)
    if a != 0:
        print(a)
    i = 1
    c = 0
    while c != b:
        if i != a and m + 1 - i != a:
            print(i)
            print(m + 1 - i)
            c += 1
        i += 1