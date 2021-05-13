import sys
input = sys.stdin.readline
sys.setrecursionlimit(250000)


def read():
    N, A, B, C, D = map(int, input().strip().split())
    S = input().strip()
    return N, A-1, B-1, C-1, D-1, S


def check_reachable(N, S, start):
    reachable = [False for s in S]
    reachable[start] = True
    
    def _bfs(x):
        for d in [1, 2]:
            nx = x + d
            if 0 <= nx < N and not reachable[nx] and S[nx] == ".":
                reachable[nx] = True
                _bfs(nx)
    
    _bfs(start)
    return reachable


def solve(N, A, B, C, D, S):
    r1 = check_reachable(N, S, A)
    r2 = check_reachable(N, S, B)
    if r1[B] and r2[D]:
        if C < D:
            return "Yes"
        else:
            for i in range(B, D+1):
                if r2[i] and 0 <= i-1 < N and 0 <= i+1 < N and r1[i-1] and r1[i+1]:
                    return "Yes"
    return "No"
        


if __name__ == '__main__':
    inputs = read()
    print(solve(*inputs))
