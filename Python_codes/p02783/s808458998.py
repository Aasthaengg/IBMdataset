import math

def main():
  H, A = map(int, input().split())
  
  ans = math.ceil(H / A)
  
  print(ans)
  
  
main()