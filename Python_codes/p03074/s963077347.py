def solve():
    N,K = map(int,input().split())
    S = input()

    one_zero = []
    target = '1'
    cnt = 0
    for i in range(N):
        if S[i] != target:
            one_zero.append(cnt)
            target = '1' if target == '0' else '0'
            cnt = 1
        else:
            cnt += 1
    else:
        one_zero.append(cnt)
        if target == '1':
            one_zero.append(0)
    
    start = 0
    end = 2*K+1
    sm = sum(one_zero[start:end])
    ans = sm
    while end < len(one_zero)*2:
        sm = sm - sum(one_zero[start:start+2]) + sum(one_zero[end:end+2])
        ans = max(ans,sm)
        start += 2
        end += 2

    print(ans)

if __name__ == '__main__':
    solve()