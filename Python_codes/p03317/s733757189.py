def main():
  n, k = map(int, input().split())
  m = 1 + (n - k) // (k - 1)
  if (n - k) % (k - 1) == 0:
    print(m)
  else:
    print(m + 1)
if __name__=="__main__":
  main()
