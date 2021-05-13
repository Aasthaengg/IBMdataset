def resolve():
    from collections import deque
    S = deque(input())
    T = deque(input())
    for i in range(len(S)):
        S.rotate(1)
        if list(S) == list(T):
            print("Yes")
            return
    print("No")


resolve()
