n,m = map(int, input().split())
sub_list = [list(input().split()) for _ in range(m)]

penalty_list = [0]*n #問題ごとのACが出るまでのペナルティ数
result_list = [0]*n #問題ごとの最終的にACが出たかどうかのリスト

for i in range(m):
  if sub_list[i][1] =='AC':
    result_list[int(sub_list[i][0]) -1] = 1
  else:
    if result_list[int(sub_list[i][0]) -1] == 0:
      penalty_list[int(sub_list[i][0]) -1] += 1

ac_count = 0
wa_count = 0
for i in range(n):
  if result_list[i] == 1:
    ac_count += 1
    wa_count += penalty_list[i]

print(f'{ac_count} {wa_count}')
