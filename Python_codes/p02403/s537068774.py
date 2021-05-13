while True:
   a,b = map(int, raw_input().split())

   if a + b ==0:
      break
    
   else:
      for i in range(a):
         print b*'#'
      print ""