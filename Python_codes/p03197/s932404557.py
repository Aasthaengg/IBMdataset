def Z(): return int(input())
def ZZ(): return [int(_) for _ in input().split()]

def main():
  N = Z()
  A = [Z() for _ in range(N)]
  print('first' if any([a%2 == 1 for a in A]) else 'second')
  return

if __name__ == '__main__':
  main()