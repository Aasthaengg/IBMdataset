from collections import deque


def solve(a):
    ans = deque()

    for i, aa in enumerate(a):
        if i % 2 == 0:
            ans.append(str(aa))
        else:
            ans.appendleft(str(aa))

    if len(a) % 2 == 1:
        ans.reverse()

    return list(ans)


if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    print(' '.join(solve(a)))
