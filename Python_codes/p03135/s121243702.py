import sys
def input(): return sys.stdin.readline().strip()

def main():
    t,x=map(int,input().split())
    print(t/x)

main()