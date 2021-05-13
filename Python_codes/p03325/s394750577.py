def log2(n):
    n = int(n)
    cnt = 0
    while ~n & 1:
        cnt += 1
        n >>= 1
    return cnt


N = int(input())
print(sum(map(log2, input().split())))
