if __name__ == '__main__':
    from collections import deque

    n = int(input())
    A = deque([])
    for i in range(n):
        command = input()
        if command[6] == "F":
            A.popleft()
        elif command[6] == "L":
            A.pop()
        elif command[0] == "i":
            A.appendleft(int(command[7:]))
        else:
            try:
                A.remove(int(command[7:]))
            except ValueError:
                continue

    print(*A)

