N, M = map(int, input().split())
study_days = map(int, input().split())

# リストにM個の数字を、入力したい
# study_days_list = []
# study_days_list.append(study_days)
# print(study_days_list)

total_study_days = sum(study_days)

answer = (N - total_study_days)

if answer < 0:
    print(-1)
else:
    print(answer)