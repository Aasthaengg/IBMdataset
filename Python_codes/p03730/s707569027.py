def ans(a, b, c) : 
  if c == 0 : 
    print('YES')
    
  elif a % b == 0 : 
    print('NO')
    
  else : 
    d = a % b
    for i in range(b) : 
      if (d * i) % b == c :
        print('YES')
        return
    print('NO')

a, b, c = tuple(map(int, input().split()))

ans(a, b, c)

