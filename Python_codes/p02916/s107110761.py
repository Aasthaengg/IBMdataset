N = int(input())
buffet = [int(i) for i in input().split()]
satisfaction_level_B = [int(i) for i in input().split()]
satisfaction_level_C = [int(i) for i in input().split()]
count = []
result = 0

for i in buffet:
    count.append(i)
    result += satisfaction_level_B[i - 1]
    if len(count) >= 2:
        if count[-1] - count[-2] == 1:
            result += satisfaction_level_C[i - 2]
print(result)