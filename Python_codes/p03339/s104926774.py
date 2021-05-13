N = int(input())
S = input()

total = 0
 
total_list = []

# 事前に計算しておく
count_w_from_left = [0]
pre_count = 0
for i in range(1, N):
  if S[i-1:i] == 'W':
    pre_count += 1
  count_w_from_left.append(pre_count)

count_e_from_right = []
for i in range(N):
  count_e_from_right.append(0)
pre_count = 0
for i in range(N - 2, -1, -1):
  if S[i+1:i+2] == 'E':
    pre_count += 1
  count_e_from_right[i] = pre_count

# 算出処理
for i in range(N):
    to_E = count_w_from_left[i]
    to_W = count_e_from_right[i]
    total_list.append(to_E + to_W)
 
print(min(total_list))