n, m = map(int, input().split())
data = list(map(int, input().split()))
ans = max(data)
print(max(0, 2*ans-n-1))