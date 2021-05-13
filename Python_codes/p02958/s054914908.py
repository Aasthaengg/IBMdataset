N = int(input())
p = list(map(int, input().split()))
isMatch = list(map(lambda x, y: x == y, p, sorted(p)))
result = 'YES' if isMatch.count(False) <= 2 else 'NO'
print(result)