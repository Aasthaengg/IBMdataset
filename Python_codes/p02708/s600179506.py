N,K = map(int,input().split())
# ln = []
# for n in range(N + 1):
#     ln.append(n)
s = 0
f = N * (N + 1) / 2
for k in range(K,N + 2):
    # mx = sum(ln[N - k + 1:N + 1])
    # mn = sum(ln[0:k]) - 1
    mx = int(f - (N - k) * (N - k + 1) / 2)
    mn = int((k - 1) * k / 2) - 1
    m = mx - mn
    s += m
    s = s % (10 ** 9 + 7)
print(s)
