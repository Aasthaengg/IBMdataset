N = int(input())
cnt = 1
answer = 0
div = 10
if N % 2 == 0:
    while div <= N:
        answer += N//div
        div *= 5
print(answer)