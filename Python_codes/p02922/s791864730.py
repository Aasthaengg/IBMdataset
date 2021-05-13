import sys
import math
def IL(): return map(int,sys.stdin.readline().rstrip().split())

def Main():
    a,b = IL()
    print(math.ceil((b-1)/(a-1)))
    return

if __name__=='__main__':
    Main()