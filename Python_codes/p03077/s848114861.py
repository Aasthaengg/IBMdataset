import sys
import math
def I(): return int(sys.stdin.readline().rstrip())

def Main():
    n,a,b,c,d,e = I(),I(),I(),I(),I(),I()
    mini = min(a,b,c,d,e)
    tn = math.ceil(n/mini)
    print(tn+4)
    return

if __name__=='__main__':
    Main()