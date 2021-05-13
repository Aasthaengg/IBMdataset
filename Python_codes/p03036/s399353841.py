import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10**8)
INF = float('inf')
MOD = 10**9+7


def main():
  r, D, x = map(int, readline().split())
  for _ in range(10):
    x = r*x -D
    print(x)
  
  
if __name__ == '__main__':
  main()