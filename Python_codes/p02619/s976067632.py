def score(day, contest, prev_list, loss_list, satisfied_matrix):
    plus = satisfied_matrix[day][contest]
    minus = 0
    for type, prev in enumerate(prev_list):
        spend = day - prev
        minus += loss_list[type] * spend

    return plus - minus



days = int(input())
loss_list = list(map(int, input().split()))
satisfied_matrix = [list(map(int, input().split())) for _ in range(days)]

prev_list = [-1] * 26

total = 0
for day in range(days):
    contest = int(input())
    prev_list[contest-1] = day
    total += score(day, contest-1, prev_list, loss_list, satisfied_matrix)
    print(total)