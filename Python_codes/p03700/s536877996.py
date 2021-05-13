from math import ceil
def solve():
    N, A, B = map(int, input().split())
    H = [int(input()) for _ in range(N)]
    top = max(H)
    total = sum(H)
    bottom = 0
    mid = (top+bottom)//2
    while bottom+1<top:
        cnt = 0
        for i in range(N):
            cnt += max(ceil((H[i]-B*mid)/(A-B)),0)
        if cnt>mid:
            bottom = mid
        else:
            top = mid
        mid = (top+bottom)//2
    ans = top
    return ans
print(solve())