N, K = map(int, input().split())
A = list(map(int, input().split()))
A_dict = dict()
for i in range(N):
    if A_dict.get(A[i]) is None:
        A_dict[A[i]] = 1
    else:
        A_dict[A[i]] += 1
A_dict_len = len(A_dict.keys())
ans = 0
A_dict_sorted = sorted(A_dict.items(), key=lambda a: a[1])
#print(A_dict_sorted)
for i in range(max(0, A_dict_len - K)):
    ans += A_dict_sorted[i][1]
print(ans)
