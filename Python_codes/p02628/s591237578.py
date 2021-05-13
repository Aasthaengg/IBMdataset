n, k = map(int,input().split())
data = sorted([int(i) for i in input().split()], reverse = False)
ans = 0

ans = sum(data[:k])
print(ans)