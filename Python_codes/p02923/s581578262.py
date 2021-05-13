import sys

sys.setrecursionlimit(10 ** 8)

input = sys.stdin.readline


def main():
    N = int(input())
    H = [int(x) for x in input().split()]

    cnt = 0
    prev = H[0]
    ans = 0
    for i in range(1, N):
        if prev >= H[i]:
            cnt += 1
        else:
            ans = max(ans, cnt)
            cnt = 0
        prev = H[i]

    ans = max(ans, cnt)
    print(ans)


    

if __name__ == '__main__':
    main()

