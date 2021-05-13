def solve():
  X, A, B = [int(input()) for i in range(3)]
  return (X - A) % B

if __name__ == '__main__':
  print(solve())