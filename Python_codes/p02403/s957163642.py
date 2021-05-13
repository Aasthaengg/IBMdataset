while True :
  H, W = map(int, input().split())
  if(H == 0 & W == 0) :
    break
  else :
    for i in range(H) :   #i in range(x) 1つずつカウント。i <= x
      for i in range(W) :
        print("#", end = "")   #最後だけ空白無し
      print()   #改行
    print()
