import sys
readline = sys.stdin.readline

def solve():
    N, K = map(int, readline().split())
    P = [v - 1 for v in map(int, readline().split())]
    C = list(map(int, readline().split()))


    ans = -10**10

    for i in range(N):
        moves = 1
        cur = P[i]
        score = C[cur]
        ans = max(score, ans)
        visited = {cur: (moves, score)}

        while P[cur] not in visited and moves < K:
            cur = P[cur]
            moves += 1
            score += C[cur]
            visited[cur] = (moves, score)

            ans = max(ans, score)
        
        if moves == K:
            continue
        
        cur = P[cur]
        moves += 1
        score += C[cur]

        T = moves - visited[cur][0]
        D = score - visited[cur][1]

        if D < 0:
            continue
        
        nloops = K - moves
        moves += T * (nloops // T)
        score += D * (nloops // T)

        ans = max(ans, score)

        while moves < K:
            cur = P[cur]
            moves += 1
            score += C[cur]
            ans = max(ans, score)
    
    print(ans)

solve()