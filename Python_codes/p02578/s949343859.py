N = int(input())
A = list(map(int, input().split()))
answer = 0
prev = 0
for a in A:
    step = max(0, prev - a)
    answer += step
    prev = a + step
print(answer)