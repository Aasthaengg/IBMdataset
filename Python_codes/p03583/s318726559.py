def main(n):
  if n%2==0:
    print(n,n,n//2)
    exit()
  if n==3:
    print(2,2,3)
    exit()
  s=n//4
  for i in range(2*s,3500*2):
    for a in range(s,i-3):
      b=i-a
      c=a*b*n/(4*a*b-n*b-n*a)
      if float.is_integer(c) and c>0:
        print(a,b,int(c))
        exit()

if __name__=='__main__':
  import sys
  input = sys.stdin.readline
  n=int(input())
  main(n)