def resolve():
    from collections import deque
    N = int(input())
    A = [int(i) for i in input().split()]
    ans = deque()
    for i in range(N):
        if i % 2 == 0:
            ans.append(A[i])
        else:
            ans.appendleft(A[i])
    if i % 2 == 0:
        print(*list(ans)[::-1])
    else:
        print(*ans)


resolve()
