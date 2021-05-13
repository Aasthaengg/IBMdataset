import sys
input = sys.stdin.readline
def main():
    N = int(input())
    P = [int(input()) for i in range(5)]
    NEC = min(P)
    ans = (N+NEC-1)//NEC + 4
    print(ans)

if __name__ == '__main__':
    main()