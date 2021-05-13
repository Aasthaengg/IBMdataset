import itertools
import fractions
def main():
  r = int(input())
  if r < 1200:
    print("ABC")
  elif 1200 <= r < 2800:
    print("ARC")
  else:
    print("AGC")
if __name__ == '__main__':
  main()