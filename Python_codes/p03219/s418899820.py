import sys
input = sys.stdin.readline

def main():
    x, y = map(int, input().split())

    print(x+y//2)

main()