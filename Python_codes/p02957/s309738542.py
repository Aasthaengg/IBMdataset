import sys


def input():
    return sys.stdin.readline().strip()

def main():
    a, b = map(int, input().split())
    if abs(a-b) % 2 != 0:
        print("IMPOSSIBLE")
        return
    if a >= b:
        print((a-b)//2+b)
        return
    print((b-a)//2+a)
    
main()
