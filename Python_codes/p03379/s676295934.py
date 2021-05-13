N = int(input())
sorted_X = sorted([(v, i) for i, v in enumerate(map(int, input().split()))])
med_former = sorted_X[N // 2][0]
med_latter = sorted_X[N // 2 - 1][0]
ans = [-1] * N
for j, (v, i) in enumerate(sorted_X):
    if j < N // 2:
        ans[i] = med_former
    else:
        ans[i] = med_latter
print("\n".join(map(str, ans)))
