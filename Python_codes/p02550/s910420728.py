n, x, m = map(int, input().split())
X = [-1] * m
P = []
sum_p = 0
while X[x] < 0: # preset
    X[x] = len(P) # pre length
    P.append(sum_p) # pre sum_p
    sum_p += x # now sum_p
    x = x*x % m
cyc_times, nxt_len = divmod(n - X[x], len(P) - X[x])
cyc = (sum_p - P[X[x]]) * cyc_times
remain = P[X[x] + nxt_len]
print(cyc + remain)
