from collections import deque

def main():
    R,C= map(int,input().split())

    S = [0,0]

    mv = [[1,0],[-1,0],[0,-1],[0,1]]
    MAP = []
    flg = 0
    block = 0
    for _ in range(R):
        t = list(input())
        block += t.count('#')
        MAP.append(t)
    stack = deque([S])
    MAP_c = [[None]*C for _ in range(R)]
    MAP_c[0][0] = 1
    while stack:
        v = stack.popleft()
        for m in mv:
            u = [v[0]+m[0],v[1]+m[1]]
            if u[0] >=0 and u[0] < R and u[1] >= 0 and u[1] < C and MAP[u[0]][u[1]] == '.':
                MAP[u[0]][u[1]] = '#'
                MAP_c[u[0]][u[1]] = MAP_c[v[0]][v[1]] + 1
                stack.append(u)
                if u == [R-1,C-1]:
                    flg = 1

        if flg == 1:
            break

    if flg == 1:
        a = MAP_c[R-1][C-1]
        print(R*C - a - block)
    else:
        print(-1)


main()