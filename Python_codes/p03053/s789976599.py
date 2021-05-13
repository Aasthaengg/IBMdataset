from collections import deque
def main():
    h, w = map(int, input().split())
    A = [list(input()) for _ in range(h)]
    B = [(i, j) for i, a in enumerate(A) for j, b in enumerate(a) if b == '#']
    dxy = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    stack = deque(B)
    colored = len(B)
    tot = h * w
    count = 0
    while colored < tot:
        next = deque([])
        while stack:
            y, x = stack.popleft()
            for dx, dy in dxy:
                X = x + dx
                Y = y + dy
                if X < 0 or X >= w or Y < 0 or Y >= h:
                    continue
                if A[Y][X] == '.':
                    next.append((Y, X))
                    A[Y][X] = '#'
        stack = next
        count += 1
        colored += len(next)
    print(count)

if __name__ == '__main__':
    main()
