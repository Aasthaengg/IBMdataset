def main():
  result = 0
  k, s = map(int, input().split())
  for x in range(k + 1):
    for y in range(k + 1):
      z = s - x - y
      if 0 <= z <= k:
        result += 1
  print(result)
if __name__ == "__main__":
  main()