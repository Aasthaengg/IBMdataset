from itertools import accumulate

n = int(input())
arr = list(map(int, input().split()))

arr.sort()

# 1つ前までの累積和の2倍がその時点の要素の大きさに達しているかどうか
cumsum = list(accumulate(arr))

result = []
for x, y in zip(arr[1:], cumsum[:-1]):
    if x <= y * 2:
        result.append(True)
    else:
        result.append(False)

if all(result):
    ans = n
else:
    ans = result[::-1].index(False) + 1

print(ans)