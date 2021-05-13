S = input()
answer = 0
for i in range(4):
    if S[i] == '+':
        answer = answer + 1
    else:
        answer = answer - 1
print(answer)