N, A, B = map(int, input().split())
ans = 0
for i in range(1,N+1):
    T = str(i)
    T_sum = 0
    for t in T:
        T_sum += int(t)
    if A <= T_sum <= B:
        ans += i
print(ans)
