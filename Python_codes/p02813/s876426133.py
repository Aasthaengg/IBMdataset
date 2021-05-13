
import itertools

def solve():
    N = int(input())
    P = tuple(map(int, input().split()))
    Q = tuple(map(int, input().split()))
    l = [i for i in range(1, N+1)]
    p = tuple(itertools.permutations(l))
    P_index = p.index(P)
    Q_index = p.index(Q)
    print(abs(Q_index - P_index))


if __name__ == "__main__":
    solve()