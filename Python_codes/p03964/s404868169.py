def solve():
    N = int(input())

    now_t, now_a = 1,1
    for _ in range(N):
        t, a = map(int,input().split())
        n = max(-(-now_t//t), -(-now_a//a))
        now_t = t * n
        now_a = a * n
    
    print(now_t + now_a)
    
if __name__ == '__main__':
    solve()