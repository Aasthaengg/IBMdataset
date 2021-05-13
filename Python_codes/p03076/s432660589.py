A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())
answer = 0
cooking_time_order = sorted([A, B, C, D, E], key=lambda x: 10 - (x % 10))
for _ in range(5):
    if cooking_time_order[-1] % 10 == 0:
        answer += cooking_time_order[-1]
        cooking_time_order.pop()
    else:
        break
if len(cooking_time_order) == 0:
    pass
else:
    for cooking_time in cooking_time_order[:-1]:
        answer += (cooking_time + (10 - (cooking_time % 10)))
    answer += (cooking_time_order[-1])
print(answer)
