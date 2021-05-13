N, K, S = map(int, input().split())
ans = [str(S)] * K

if S == 1e9:
    ans = ans + ['1'] * (N - K)
else:
    ans = ans + [str(S + 1)] * (N - K)
print(' '.join(ans))