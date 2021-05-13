n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

shortage = [b - a for a, b in zip(A, B) if a < b]
over = sorted([a - b for a, b in zip(A, B) if a > b], reverse=True)

sum_shortage = sum(shortage)
sum_over = 0
count = -1
if sum_shortage == 0:
    count = 0
elif sum_shortage > sum_over:
    for i, v in enumerate(over):
        sum_over += v
        if sum_shortage <= sum_over:
            count = len(shortage) + i + 1
            break
print(count)