N, K = map(int, input().split())
S = input()

def calc_happiness(S):
    cnt = 0
    for i in range(1, len(S)):
        if S[i-1] == S[i]:
            cnt += 1
    return cnt

print(min(N-1, calc_happiness(S)+ K*2))
