import sys

sys.setrecursionlimit(10 ** 8)

input = sys.stdin.readline


def main():
    N = int(input())
    A = [int(x) for x in input().split()]

    prev = A[0]
    ans = 0
    for a in A[1:]:
        if prev == a:
            ans += 1
            prev = -1
        else:
            prev = a

    print(ans)


    

if __name__ == '__main__':
    main()

