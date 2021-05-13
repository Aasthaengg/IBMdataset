def solve():
    N = int(input())
    AB = [list(map(int, input().split())) for _ in range(N)]
    ret = 0
    total = 0
    for i in range(N)[::-1]:
        diff = (-1*(AB[i][0]+ret))%AB[i][1]
        ret += diff
        
    print(ret)
    
solve()