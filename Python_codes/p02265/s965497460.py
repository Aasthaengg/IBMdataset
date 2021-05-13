def resolve():
    from collections import deque
    n = int(input())
    que = deque()
    for _ in range(n):
        cv = input().split()
        if cv[0] == "insert":
            x = int(cv[1])
            que.appendleft(x)
        elif cv[0] == "delete":
            x = int(cv[1])
            if x in que:
                que.remove(x)
        elif cv[0] == "deleteFirst":
            que.popleft()
        elif cv[0] == "deleteLast":
            que.pop()
    ans = list(que)
    print(*ans)


resolve()

