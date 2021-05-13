def main():
  s = input()
  K = int(input())
  a = set()
  for i in range(len(s)):
    for j in range(1, 6):
      a.add(s[i:i+j])
  print(sorted(list(a))[K-1])
  return

if __name__ == '__main__':
  main()