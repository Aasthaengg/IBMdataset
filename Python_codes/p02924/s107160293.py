def main():
    import sys
    sys.setrecursionlimit(10**9)
    input = sys.stdin.readline

    N = int(input())

    print(N*(N-1)//2)

main()