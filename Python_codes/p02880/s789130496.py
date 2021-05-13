from sys import exit
def main():
  N = int(input())
  
  for i in range(9,0,-1):
    if N % i == 0 and N / i < 10:
      print('Yes')
      exit()
    
  print('No')
    
  
  
  
main()