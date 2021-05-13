n, x, t = map(int, input().split())
answer = 0
while n > 0:
    n -= x
    answer += t
print(answer)
