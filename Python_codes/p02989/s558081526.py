N = int(input())
d = sorted(list(map(int, input().split())))

center_idx = N // 2
if d[center_idx-1] == d[center_idx]:
    print(0)
else:
    print(d[center_idx] - d[center_idx-1])