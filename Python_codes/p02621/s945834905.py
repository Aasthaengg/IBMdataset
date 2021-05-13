from sys import stdin
input = stdin.readline
ri = lambda : int(input())
ril = lambda : list(map(int, input().split()))

def main():
  a = ri()
  a = a * (a * (a + 1) + 1)
  print(a)


if __name__ == '__main__':
  main()
