L, R, d = map(int, input().split())
print(sum(num  % d == 0 for num in range(L, R + 1)))