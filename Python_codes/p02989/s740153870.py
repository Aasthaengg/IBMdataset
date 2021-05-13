def main():
  N = int(input())
  if N % 2 == 1:
    print(0)
    return 0
  
  num = int(N/2)
  D = list(map(lambda d: int(d), input().split(" ")))
  D.sort()
  
  difficultABC = D[int(N/2) - 1]
  easyARC = D[int(N/2)]
# difficultABC < K <= easyARC
  print(easyARC - difficultABC)

main()