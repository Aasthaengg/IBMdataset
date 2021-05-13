a, b, c = map(int, input().split())

sum = a + b + c
max = max([a, b ,c])

answer = sum - max
print(answer)