def solve():
    N,M = map(int,input().split())
    hostile = []
    for _ in range(M):
        a, b = map(int,input().split())
        hostile.append((a,b))
    
    hostile.sort(key=lambda x:x[1])
    ans = 0
    last_cut = -1
    for a,b in hostile:
        if last_cut < a:
            last_cut = b-1
            ans += 1
    
    print(ans)
        
if __name__ == '__main__':
    solve()