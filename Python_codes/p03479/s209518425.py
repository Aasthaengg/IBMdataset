# one example of valid A is {X, (2 * X), (2 * 2 * X), ...}
X, Y = list(map(int, input().split()))
answer = 0
while X <= Y:
    answer += 1
    X *= 2
print(answer)