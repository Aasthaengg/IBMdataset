def solve():
    N = int(input())
    S = input()
    white = [0] * (N+1)
    black = [0] * (N+1)
    for i in range(1,N+1):
        if S[i-1] == '.':
            white[i] = white[i-1] + 1
            black[i] = black[i-1]
        else:
            black[i] = black[i-1] + 1
            white[i] = white[i-1]
    
    ans = float('inf')
    for i in range(N+1):
        tmp = black[i] + white[-1] - white[i]
        ans = min(ans, tmp)
    
    print(ans)
    
if __name__ == '__main__':
    solve()