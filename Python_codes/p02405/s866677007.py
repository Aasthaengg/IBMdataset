while True:
    h1 = ""
    h2 = ""
    H,W = map(int, input().split())
    if H == 0 and W == 0:
        break

    for j in range(W):
      if j%2 == 0:
        h1 = h1 + "#"
      else:
        h1 = h1 + "."
    for j in range(W):
      if j%2 == 0:
        h2 = h2 + "."
      else:
        h2 = h2 + "#"
    
    for i in range(H):
        if i%2 == 0:
            print(h1)
        else:
            print(h2)
    print()