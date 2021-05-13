def solve():
    from collections import deque
    from sys import stdin
    f_i = stdin
    
    N, M = map(int, f_i.readline().split())
    S = f_i.readline().rstrip()
    
    pos = N
    rec = deque()
    while pos:
        for move in range(M, 0, -1):
            next_pos = pos - move
            if next_pos >= 0 and S[next_pos] == '0':
                pos = next_pos
                rec.appendleft(move)
                break
        else:
            print(-1)
            break
    else:
        print(' '.join(str(move) for move in rec))

solve()