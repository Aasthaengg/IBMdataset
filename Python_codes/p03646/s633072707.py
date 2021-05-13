K = int(input())
m = K%50
n = K//50
ans = list(range(51-m,51)) + list(range(50-m))
ans = [n+a for a in ans]
print(50)
print(*ans)