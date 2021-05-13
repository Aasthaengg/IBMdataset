n, k = map(int, input().split())
n_list = []
a_int_all = []
for i_n in range(1, n + 1):
    n_list.append(i_n)
for i in range(0, k):
    d_k = input()
    a_int_k = list(map(int, input().split()))
    a_int_all.extend(a_int_k)
n_only = set(a_int_all)
ans = n - len(n_only)
print(ans)