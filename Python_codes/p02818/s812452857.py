def main():
  A, B, K = map(int, input().split())
  
  if K <= A:
    print(A - K, B)
  elif K > A and B >= K - A:
    print(0, B - (K - A))
  elif K > A and B < (K - A):
    print(0, 0)
  
  
  
main()