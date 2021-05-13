N, A, B = map(int, input().split())

ans = 0

for n in range(1, N+1, 1):
    l = [i for i in str(n)]
    n_sum = sum(map(int, l))
    if n_sum >= A and n_sum <= B:
        ans += n

print(ans)