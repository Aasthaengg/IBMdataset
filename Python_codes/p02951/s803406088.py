import sys


def input():
    return sys.stdin.readline().strip()

def main():
    a, b, c = map(int, input().split())
    if a-b>=c:
        print(0)
        return
    print(c-a+b)
    
main()
