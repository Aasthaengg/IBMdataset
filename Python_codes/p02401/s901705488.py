while True:
  a,op,b = input().split()
  a=int(a)
  op=str(op)
  b=int(b)
  
  if op=='?':
    break
  elif  op=='+':
    print("{:d}".format(a+b))
  elif op=='-':
    print("{:d}".format(a-b))
  elif op=='/':
    print("{:d}".format(a//b))
  elif op=="*":
    print("{:d}".format(a*b))
