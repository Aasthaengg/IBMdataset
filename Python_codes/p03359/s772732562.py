import sys
def input(): return sys.stdin.readline().strip()

def main():
    a,b=map(int,input().split())
    print((a-1) + (b>=a))

main()