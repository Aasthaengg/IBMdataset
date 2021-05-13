answer = 0
for i in range(2):
    answer += min(int(input()) for _ in range(2))
print(answer)