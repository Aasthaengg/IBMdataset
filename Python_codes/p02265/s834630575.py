from collections import deque


def main():
    n = int(input())
    Q = deque()

    for _ in range(n):
        cmd = input().split()

        if cmd[0] == "deleteFirst":
            Q.popleft()
        elif cmd[0] == "deleteLast":
            Q.pop()
        elif cmd[0] == "insert":
            Q.appendleft(int(cmd[1]))
        elif cmd[0] == "delete" and int(cmd[1]) in Q:
            Q.remove(int(cmd[1]))

    print(*Q)


if __name__ == "__main__":
    main()

