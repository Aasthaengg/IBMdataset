int(input())
i = list(map(int, input().split()))

maxValue = max(i)
minValue = min(i)
sumValue = sum(i)

print('{} {} {}'.format(minValue, maxValue, sumValue))