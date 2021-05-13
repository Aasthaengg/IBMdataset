import sys

def main(inp):
    n,k = map(int,next(inp).split())
    return n-k+1
  
print(main(sys.stdin))