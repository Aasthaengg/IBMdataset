N, K = map(int, input().split())
R, S, P = map(int, input().split())
T = input()

tensu = {
    'r': R,
    's': S,
    'p': P
}

win = {
    'r': 'p',
    's': 'r',
    'p': 's'
}

ans = [None] * N

sum_ = 0
for i, t in enumerate(T):
    if i < K or ans[i - K] != win[t]:
        ans[i] = win[t]
        sum_ += tensu[ans[i]]

print(sum_)
