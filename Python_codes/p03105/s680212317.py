import itertools
import fractions
def main():
  a,b,c = map(int,input().split())
  print(c if a*c <= b else b//a)
if __name__ == '__main__':
  main()