N = int(input())
buffet = [int(i) for i in input().split()]
satisfaction_level_B = [int(i) for i in input().split()]
satisfaction_level_C = [int(i) for i in input().split()]
result = 0

for i in range(N):
    result += satisfaction_level_B[buffet[i] - 1]
    if i > 0:
        if buffet[i] - buffet[i - 1] == 1:
            result += satisfaction_level_C[buffet[i - 1] - 1]
print(result)