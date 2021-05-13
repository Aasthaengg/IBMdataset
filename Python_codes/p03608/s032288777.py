from sys import stdin
from itertools import permutations
def main():
    N,M,R = map(int,stdin.readline().split())
    r = list(map(int,stdin.readline().split()))
    r = tuple(map(lambda x: x-1,r))
    dist = [[2**60]*N for _ in range(N)]
    for _ in range(M):
        A,B,C = map(int,stdin.readline().split())
        A -= 1
        B -= 1
        dist[A][B] = C
        dist[B][A] = C
    for i in range(N):
        dist[i][i] = 0
    for k in range(N):
        for i in range(N):
            for j in range(N):
                dist[i][j] = min(dist[i][j],dist[i][k]+dist[k][j])
    dist = tuple(map(lambda x: tuple(x),dist))
    ans = 2**60
    for t in tuple(permutations(r,R)):
        tmp = 0
        for i in range(R-1):
            tmp += dist[t[i]][t[i+1]] 
        ans = min(ans,tmp)
    
    print(ans)

if __name__ == "__main__":
    main()