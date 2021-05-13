k, t = map(int, input().split())
arr = [int(x) for x in input().split()]

m = max(arr)
ans = m*2 - k - 1

print(max(0, ans))
