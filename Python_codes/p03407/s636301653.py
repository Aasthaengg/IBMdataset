import sys
def input(): return sys.stdin.readline().strip()

def main():
    a,b,c=map(int,input().split())
    print('Yes' if a+b>=c else 'No')

main()