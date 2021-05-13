import sys

def input():
    return sys.stdin.readline().strip()

def main():
    a, b = map(int, input().split())
    if a > b:
        print(2*a-1)
        return
    if b > a:
        print(2*b-1)
        return
    if a == b:
        print(a+b)
    

main()