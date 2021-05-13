from sys import exit
def main():
  A, B = map(int, input().split())
  
  if A % B == 0:
    print(A)
    exit()
  elif B % A == 0:
    print(B)
    exit()
  elif A == B :
    print(A)
    exit()
    
  large = 0
  small = 0
  if A > B:
    large = A
    small = B
  else:
    large = B
    small = A
    
  i = 2
  while True:
    if (large * i) % small == 0:
      print(large * i)
      exit()
    i += 1
  
  
  
  
  
main()