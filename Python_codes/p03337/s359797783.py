import sys
def input(): return sys.stdin.readline().strip()

def main():
    a,b=map(int,input().split())
    print(max([a+b,a-b,a*b]))

main()