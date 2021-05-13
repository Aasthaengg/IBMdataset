S = input()
K = int(input())
before = ''
count = 0
change_cnt = 0
for c in S:
  if c == before:
    count += 1
  else:
    if count >= 0:
      change_cnt += (count+1)//2
      count = 0
    before = c
if count > 0:
    change_cnt += (count+1)//2
c_cnt = 0
if S[0] == S[-1]:
  for c in S:
    if c == before:
      c_cnt += 1
    else:
      break
all_same = False
plus = False
if count%2 == 0 and c_cnt%2 != 0:
  plus = True
if count+c_cnt >= len(S):
  all_same = True
# print(all_same, plus, count, change_cnt, c_cnt)  
if all_same:
  print((K//2)*len(S) + (K%2)*(len(S)//2))
elif plus:
  print(K*change_cnt + K-1)
else:
  print(K*change_cnt)
  
  
