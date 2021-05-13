import sys
input = sys.stdin.readline


def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    import collections
    D = collections.deque(A)
    ans = []
    for i in range(N-1):
        a, b = D.popleft(), D.pop()
        if not D or D[-1] < 0:
            D.append(b - a)
            ans.append((b, a))
        else:
            D.appendleft(a - b)
            ans.append((a, b))
    print(D.pop())
    for x, y in ans:
        print(x, y)


if __name__ == '__main__':
    main()
