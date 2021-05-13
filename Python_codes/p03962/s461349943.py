import sys
def v():
    x=[x for x in sys.stdin.readline().split()]
    print(len(set(x)))
if __name__=='__main__':v()