N, MIN, MAX = map(int, input().split())

sum_min = (N-1)*MIN + MAX
sum_max = (N-1)*MAX + MIN
# print(sum_max)
# print(sum_min)

if N > 1:
    if sum_max >= sum_min:
        print(sum_max - sum_min + 1)
    else:
        print(0)
elif N == 1:
    if MIN!= MAX:
        print(0)
    else:
        print(1)