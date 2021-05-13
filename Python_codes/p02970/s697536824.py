import sys


def input():
    return sys.stdin.readline().strip()

def main():
    n, d = map(int, input().split())
    if n % (2*d+1) == 0:
        print(n // (2*d+1))
        return
    print(n // (2*d+1)+1)
    
    

main()