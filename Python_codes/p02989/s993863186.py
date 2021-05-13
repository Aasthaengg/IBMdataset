N = int(input())
d = list(sorted(map(int, input().split())))
K_high = d[N//2]
K_low = d[N//2-1] + 1
print(K_high-K_low+1)
