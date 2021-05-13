N, A, B = map(int, input().split())
ans = 0
for n in range(1, N+1):
    n_str = str(n)
    n_lst = list(n_str)
    n_lst = list(map(int, n_lst))
    sum_ = sum(n_lst)
    if A <= sum_ and sum_ <= B:
        ans += n
print(ans)