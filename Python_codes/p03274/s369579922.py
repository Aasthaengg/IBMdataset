N, K = map(int, input().split())
x = list(map(int, input().split()))

# R = [x[i] for i in range(N) if x[i] >= 0]
# L = [abs(x[i]) for i in range(N-1, -1, -1) if x[i] < 0]

# len_R = len(R)
# len_L = N - len_R
# r = 0
# l = 0
# time = 1e10

# dp_r = [0] * (len_R + 1) #右サイドでi個選んだ時のコストdp[i]
# dp_l = [0] * (len_L + 1)

# for i in range(1, N-1):
#     dp_r[i] = min(dp_r[i-1] + R[i])
def cost(i):
    l = i
    r = i+K
    if x[l] >= 0:
        return abs(x[r-1])
    elif x[r-1] <= 0:
        return abs(x[l])
    else:
        if abs(x[l]) < abs(x[r-1]):
            return 2*abs(x[l]) + abs(x[r-1])
        else:
            return 2*abs(x[r-1]) + abs(x[l])
ans = 1e12
for i in range(0, N-K+1):
    ans = min(ans, cost(i))
print(ans)