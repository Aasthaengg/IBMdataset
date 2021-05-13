def solve():
    N, M = map(int, input().split())
    c_doubled_cnt = M // 2
    ans = 0
    if N >= c_doubled_cnt:
        ans = c_doubled_cnt
    else:
        ans = N + (c_doubled_cnt-N) // 2
    
    print(ans)

if __name__ == '__main__':
    solve()