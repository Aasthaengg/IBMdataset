import itertools
def main():
  a,b,x = map(int,input().split())
  print("YES" if a <= x and b >= (x-a) else "NO")
if __name__ == '__main__':
  main()