def main():
    INF = float('inf')
    N, M = map(int, input().split())
    dist = [0] + [INF] * (N-1)
    abc = []
    
    for i in range(M):
        a, b, c = map(int, input().split())
        abc.append((a-1, b-1, -c))
            
    for a, b, c in abc:
        dist[b] = min(dist[b], dist[a]+c)
        
    ans = dist[-1]
    
    for a, b, c in abc:
        dist[b] = min(dist[b], dist[a]+c)
            
    if ans != dist[-1]:
        print('inf')
    else:
        print(-ans)

if __name__ == '__main__':
    main()