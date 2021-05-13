N , M = map(int, input().split())
answer = 0
if M >= 2 * N:
    M -= 2 * N
    answer = N
    if M >= 4:
        answer += M // 4
else:
    answer += M // 2

print(answer)