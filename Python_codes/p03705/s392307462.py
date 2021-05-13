N, A, B = map(int,input().split())

max_s = B * (N-2)
min_s = A * (N-2)
ans = max_s - min_s + 1
if ans >= 0:
    print(max_s - min_s + 1)
else:
    print(0)