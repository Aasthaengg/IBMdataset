N, K = [int(i) for i in input().split()]
tmp = N%K
print(min(tmp, abs(tmp-K)))