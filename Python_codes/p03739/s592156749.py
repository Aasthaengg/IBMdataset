n = int(input())
A = list(map(int, input().split()))

plus_ans = 0
minus_ans = 0
sum = 0

for i in range(len(A)):
    sum += A[i]
    if i % 2 == 0:
        if sum <= 0:
            plus_ans += abs(sum) + 1
            sum = 1
    else:
        if sum >= 0:
            plus_ans += abs(sum) + 1
            sum = -1

sum = 0
for i in range(len(A)):
    sum += A[i]
    if i % 2 == 0:
        if sum >= 0:
            minus_ans += abs(sum) + 1
            sum = -1
    else:
        if sum <= 0:
            minus_ans += abs(sum) + 1
            sum = 1

print(min(plus_ans, minus_ans))
