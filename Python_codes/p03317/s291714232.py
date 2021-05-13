def main():
  n, k = map(int, input().split())
  if (n - k) % (k - 1):
    print(1 + (n - k) // (k - 1) + 1)
  else:
    print(1 + (n - k) // (k - 1) )
if __name__=="__main__":
  main()
