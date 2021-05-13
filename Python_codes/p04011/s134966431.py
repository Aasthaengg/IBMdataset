if __name__ == "__main__":
  n = int(input())
  k = int(input())
  x = int(input())
  y = int(input())

  if n <= k:
    print(int(n*x))
  else:
    print(int(k*x+(n-k)*y))
