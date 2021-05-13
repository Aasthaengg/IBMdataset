# coding: utf-8
import sys

def main(argv=sys.argv):
  
  a = int(input())
  b = int(input())
  h = int(input())
  
  print((a + b) * h // 2)
  
  
  return 0


if __name__ == '__main__':
  sys.exit(main())