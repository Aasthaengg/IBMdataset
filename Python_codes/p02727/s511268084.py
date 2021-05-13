import sys
import itertools

def main():
  x, y, a, b, c = map(int, sys.stdin.buffer.readline().split())
  red = sorted(map(int, sys.stdin.buffer.readline().split()), reverse=True)
  green = sorted(map(int, sys.stdin.buffer.readline().split()), reverse=True)
  colorless = sorted(map(int, sys.stdin.buffer.readline().split()), reverse=True)
  
  apples = sorted(itertools.chain(red[:x], green[:y], colorless), reverse=True)
  print(sum(apples[:x + y]))

main()