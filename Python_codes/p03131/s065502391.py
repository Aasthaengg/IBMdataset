k, a, b = map(int, input().split())

if a + 1 >= b:
  print(1 + k)
  
else:
  if k < a + 1:
    print(1 + k)
  else:
    
    a1 = b #a+1回
    if (k - (a + 1)) % 2 == 0:
      a2 = ((k - (a + 1)) // 2) * (b - a)
    else:
      a2 = ((k - (a + 1) - 1) // 2) * (b - a) + 1
    print(a1 + a2)