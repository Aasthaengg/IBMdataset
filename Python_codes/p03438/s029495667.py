def solve():
    N = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))

    plus2_cnt = 0
    neg_cnt = 0
    for i in range(N):
        diff = b[i] - a[i]
        if diff >= 0:
            plus2_cnt += diff // 2
        else:
            neg_cnt += abs(diff)
    
    if plus2_cnt >= neg_cnt:
        print('Yes')
    else:
        print('No')
        
if __name__ == '__main__':
    solve()
