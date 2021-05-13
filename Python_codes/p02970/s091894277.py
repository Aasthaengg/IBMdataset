def people(n):
  p=0
  while n>0:
    n-=(d*2+1)
    p+=1
  return p

def main():
  print(people(n))
  
if __name__=='__main__':
  n,d=map(int,input().split())
  main()