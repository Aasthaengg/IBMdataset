while 1:
   a, op, b = raw_input().split()
   A = int(a)
   B = int(b)
 
   if op == '?':
      break
   elif op == '+':
      print A+B
   elif op == '-':
      print A-B
   elif op == '*':
      print A*B
   elif op == '/':
      print A/B