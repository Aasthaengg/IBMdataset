import numpy as np

def main():

  W, A, B = map(int, input().split())
  
  A_ = A + W
  B_ = B + W
  
  if (A <= B and B <= A_) or (A <= B_ and B_ <= A_):
    print(0)
    return

  print(min(abs(A_ - B), abs(A - B_)))

main()