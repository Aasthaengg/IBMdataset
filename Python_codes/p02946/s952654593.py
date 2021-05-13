lst = [i for i in range(-1000000, 1000001)]
k, x = map(int, input().split())
print(*lst[x+1000000-k+1:x+1000001+k-1])
