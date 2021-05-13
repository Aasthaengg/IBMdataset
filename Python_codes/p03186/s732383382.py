import sys

def parse(inp):
    a,b,c=map(int,next(inp).split())
    return a,b,c
  
def main(inp):
    a,b,c=inp  
    if(a+b >= c-1): return b+c
    else: return a+2*b+1
    
print(main(parse(sys.stdin)))