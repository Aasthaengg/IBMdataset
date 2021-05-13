from sys import stdin

def main():
  s = []
  read = stdin.readline
  N =int(read())
  data = [list(map(int,read().split(" "))) for _ in range(N)]
  A = sorted([i[0] for i in data])
  B = sorted([i[1] for i in data])
  if N%2 == 1:
    a1 = A[((N+1)//2)-1]
    b1 = B[((N+1)//2)-1]
    print(b1 - a1 + 1)
  else:
    l = []
    a1 = A[(N//2)-1]
    b1 = B[(N//2)-1]
    a2 = A[(N//2)]
    b2 = B[(N//2)]
    print(b1 + b2 + 1 - a1 - a2)
    
  
if __name__ == "__main__":
  main()