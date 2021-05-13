from collections import deque


def main():
    n = int(input())
    As = list(map(int, input().split()))
    left = deque([])
    right = deque([])
    if n % 2 == 0:
        for i in range(n):
            if i % 2 == 0:
                right.append(As[i])
            else:
                left.appendleft(As[i])
    else:
        for i in range(n):
            if i % 2 == 0:
                left.appendleft(As[i])
            else:
                right.append(As[i])

    left.extend(right)
    print(*left)


if __name__ == "__main__":
    main()
