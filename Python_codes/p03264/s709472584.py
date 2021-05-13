K = int(input())
answer = 0
if K % 2 == 0:
    answer = (K // 2) ** 2
else:
    answer = (K // 2) * (K // 2 + 1)
print(answer)