import sys
input = sys.stdin.readline


def main():
    N = int(input())
    A = list(map(int, input().split()))
    m = sum(A)/N
    ans = []
    for i, a in enumerate(A):
        ans.append((i, abs(a-m)))
    ans.sort(key=lambda x: x[1])
    print(ans[0][0])


if __name__ == '__main__':
    main()
