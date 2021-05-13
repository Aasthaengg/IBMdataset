N = input()
array = list(map(int, input().split()))

n_max = max(array)
n_min = min(array)

ans = n_max - n_min
print(ans)