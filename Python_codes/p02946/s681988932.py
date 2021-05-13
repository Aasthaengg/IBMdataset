n, x = map(int, input().split())
lst = [i for i in range(x-n+1, x+n)]
print(*lst, sep=' ')