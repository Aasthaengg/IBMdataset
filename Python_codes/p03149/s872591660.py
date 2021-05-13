arr = list(map(int, input().split()))
arr.sort()
ans = 'YES' if ''.join([str(x) for x in arr]) == '1479' else 'NO'
print(ans)