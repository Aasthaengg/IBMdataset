# solu

n, m, k = map(int, input().split())
result = 'No'
if n + m >= k:
    result = 'Yes'
print(result)