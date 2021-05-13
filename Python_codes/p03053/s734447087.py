from collections import deque

def main():
    h, w = map(int,input().split())
    A = [list(input()) for _ in range(h)]
    B = []

    for i,a in enumerate(A):
        for j,b in enumerate(a):
            if b == "#":
                B.append((i,j))

    dxy = [[1,0],[-1,0],[0,1],[0,-1]]

    stack = deque(B)
    darked = len(stack)
    targetd = h*w
    count = 0

    while darked < targetd:
        nextd = deque([])

        while stack:
            x, y = stack.popleft()
            for dx,dy in dxy:
                X = x + dx
                Y = y + dy
                if not(0 <= X < h) or not(0 <= Y < w):
                    continue
                if A[X][Y]==".":
                    A[X][Y]="#"
                    nextd.append((X,Y))
        count += 1
        stack = nextd
        darked += len(stack)
    print(count)
    
main()
