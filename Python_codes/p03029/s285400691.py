import itertools
import fractions
def main():
  a,p = map(int,input().split())
  sur = p % 2
  print((p//2) + ((a*3)+sur)//2)
if __name__ == '__main__':
  main()