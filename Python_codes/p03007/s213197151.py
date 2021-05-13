from collections import deque


def read_int():
    return int(input().strip())


def read_ints():
    return list(map(int, input().strip().split(' ')))


def solve():
    """
    """
    N = read_int()
    B = read_ints()
    B.sort()
    A = deque(B)
    answer = []
    while len(A) > 1:
        if len(A) == 2:
            x, y = A.pop(), A.popleft()
            A.append(x-y)
        else:
            if A[-2] >= 0:
                x, y = A.popleft(), A.pop()
                A.appendleft(x-y)
            else:
                x, y = A.pop(), A.popleft()
                A.append(x-y)
        answer.append((x, y))
    print(A[0])
    for a in answer:
        print(*a)


if __name__ == '__main__':
    solve()
