from collections import deque

if __name__ == '__main__':
    l = deque()
    n = int(input())
    for _ in range(n):
        m = input().split()
        if m[0] == 'insert':
            l.appendleft(m[1])
        elif m[0] == 'delete':
            try:
                l.remove(m[1])
            except:
                pass
        elif m[0] == 'deleteFirst':
            l.popleft()
        elif m[0] == 'deleteLast':
            l.pop()
    print(' '.join(map(str, l)))

