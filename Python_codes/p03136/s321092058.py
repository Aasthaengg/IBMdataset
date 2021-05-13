N = int(input())
L = list(map(int, input().split()))

max_L = max(L)
max_i = L.index(max(L))

sum_without_max = sum([*L[:max_i], *L[max_i+1:]])

if sum_without_max > max_L:
    print("Yes")
else:
    print("No")