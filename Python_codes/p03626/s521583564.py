def abc071_d():
    N = int(input())
    S1 = str(input())
    S2 = str(input())
    MOD = 10**9 + 7
    if len(S1) == 1: return 3

    ans, sidx, prev = -1, -1, -1
    if S1[0] == S1[1]:  # 横
        ans = 6
        sidx = 2
        prev = 2
    else:  # 縦
        ans = 3
        sidx = 1
        prev = 1

    if N <= sidx: return ans
    S = S1 + '_'

    for i in range(sidx, N):
        if S[i-1] == S[i]:  # 横置きの2つ目
            continue
        if S[i] == S[i+1]:  # 横
            if prev == 1: x = 2
            else: x = 3
            prev = 2
        else:  # 縦
            if prev == 1: x = 2
            else: x = 1
            prev = 1
        ans = ans * x % MOD
    return ans

if __name__ == '__main__':
    print(abc071_d())