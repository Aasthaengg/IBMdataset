N, K = map(int, input().split())
S = input()

def solve(S):
    ans = 0
    switch = 0
    for i in range(1,N):
        if S[i]!=S[i-1]:
            switch += 1
    switch = max(0,switch-K*2)
    ans = N-switch-1
    return ans
print(solve(S))