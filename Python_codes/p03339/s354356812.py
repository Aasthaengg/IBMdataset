from sys import stdin


if __name__ == "__main__":
    _in = [_.rstrip() for _ in stdin.readlines()]
    N = int(_in[0])  # type:int
    S = list(_in[1])   # type:str
    # vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
    dp = [0]*N
    for i in range(N):
        if i==0:
            dp[i] = len([s for s in S[1:] if s=='E'])
        else:
            dp[i] = dp[i-1] + (1 if S[i-1]=='W' else 0) - (1 if S[i]=='E' else 0)
    cnt = min(dp)
    # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    print(cnt)
