n = int(input())
k = int(input())
X = list(map(int, input().split()))
ans = [2 * min(x, abs(x - k)) for x in X]
print(sum(ans))
