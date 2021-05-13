k, x = map(int, input().split())
l, r = x-k+1, x+k-1
ret = [i for i in range(l, r+1)]
print(*ret)