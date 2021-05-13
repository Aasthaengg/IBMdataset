import sys

input = sys.stdin.readline

def main():
    ans = 0
    A,B,C = map(int, input().split())
    if A*B*C%2 == 1:
        ans = min(A,B,C)*(A+B+C-(min(A,B,C)+max(A,B,C)))
    print(ans)

if __name__ == '__main__':
    main()