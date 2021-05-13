def main(a,op,b):
  if op=='+':
    return int(a)+int(b)
  elif op=='-':
    return int(a)-int(b)
 
  
if __name__=='__main__':
  a,op,b=input().split()
  print(main(a,op,b))