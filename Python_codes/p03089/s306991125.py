from queue import Queue

def solve():
    N = int(input())
    b = list(map(int, input().split()))
    idx = [i+1 for i in reversed(range(N))]
    
    l = []
    for i in range(N):
        for bi, j in zip(reversed(b), idx):
            if j == bi:
                l.append(str(j))
                break
        del idx[0], b[j-1]
    
    return '\n'.join(reversed(l)) if len(l) == N else -1

print(solve())