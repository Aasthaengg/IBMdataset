from sys import stdin

def main():
    N, K = map(int, stdin.readline().rstrip().split())

    if K == 1:
      print(0)
    else:
      print(N-K)

main()

