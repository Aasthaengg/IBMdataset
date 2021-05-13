k, x = map(int, input().split())
left = max(-1000000, x-k+1)
right = min(1000000, k+x-1)
if k == 1:
    print(x)
else:
    print(' '.join(list(map(str, list(range(left, right+1))))))