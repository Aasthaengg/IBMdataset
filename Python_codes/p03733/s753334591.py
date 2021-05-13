n, T = [int(i) for i in input().split()]
t = [int(i) for i in input().split()]
start = 0
stop = 0
ans = 0
for i in range(len(t)):
    start = max(stop, t[i])
    stop = t[i] + T
    ans += stop - start
print(ans)