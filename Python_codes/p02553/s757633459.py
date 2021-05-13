number = list(map(int, input().split(" ")))

answer = []

answer.append(number[0] * number[2])
answer.append(number[0] * number[3])
answer.append(number[1] * number[2])
answer.append(number[1] * number[3])

print(max(answer))