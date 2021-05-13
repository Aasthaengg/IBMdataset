from collections import deque

def doubly(n):
    list = deque()
    for i in range(n):
        line = input().split()
        p = line[0]
        while True:
            try:
                key = line[1]
                break
            except IndexError:
                break
        if p == "insert":
            list.appendleft(key)
        elif p == "deleteFirst":
            list.popleft()
        elif p == "deleteLast":
            list.pop()
        else:
            while True:
                try:
                    list.remove(key)
                    break
                except ValueError:
                    break
    print(' '.join(list))

if "__main__" == __name__:
    n = int(input())
    doubly(n)

