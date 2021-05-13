def solve():
    K = int(input())
    lunluns = []
    for i in range(1,10):
        dfs(1,i,lunluns)
    
    lunluns.sort()
    print(lunluns[K-1])

def dfs(d,now,lunluns):
    lunluns.append(now)

    if d == 10:
        return
    
    for i in [-1,0,1]:
        add = now % 10 + i

        if 0 <= add <= 9:
            dfs(d+1,now*10+add, lunluns)
        
if __name__ == '__main__':
    solve()
