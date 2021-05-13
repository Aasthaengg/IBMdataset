if __name__ == "__main__":
  n,k = map(int,input().split())
  ans = int(k*((k-1)**(n-1)))
  print(ans)
