
from sys import exit
def main():
  A = int(input())
  B = int(input())
  
  ans = [1,2,3]
  
  ans.remove(A)
  ans.remove(B)
  
  print(str(ans).replace('[', '').replace(']', ''))
  
  
main()