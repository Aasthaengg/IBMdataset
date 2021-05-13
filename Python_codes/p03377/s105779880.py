import sys
input = sys.stdin.readline

def main():
    A, B, X = map(int, input().split())
    if A > X:
        print("NO")
    elif A + B < X:
        print("NO")
    else:
        print("YES")

if __name__ == '__main__':
    main()