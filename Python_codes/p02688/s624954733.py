def main():
  n, k = map(int, input().split())
  a = set()
  for i in range(k):
    input()
    a |= set(list(map(int, input().split())))
  print(n-len(a))

if __name__ == "__main__":
  main()