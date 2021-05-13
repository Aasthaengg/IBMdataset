#!/usr/bin/python3

def main():
  n, k = map(int, input().split(' '))
  if k == 1:
    print(0)
    return

  print(n - k)
  return

if __name__ == '__main__':
  main()