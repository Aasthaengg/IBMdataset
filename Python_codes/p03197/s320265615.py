def main():
  import sys
  pin=sys.stdin.readline
  pout=sys.stdout.write
  perr=sys.stderr.write
  
  N=int(pin()[:-1])
  m=0
  for i in range(N):
    a=int(pin()[:-1])
    if a%2==0:
      m+=1
  if m==N:
    print("second")
  else:
    print("first")
    return 
main()