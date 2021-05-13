def main():
  K, S = list(map(int, input().split()))
  counter = 0
  for i in range(K+1):
    for j in range(K+1):
      if (0<=S-i-j<=K):
        counter += 1

  print(counter)


if(__name__ == '__main__'):
  main()