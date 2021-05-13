S = input()

s_list = [s for s in S]
c_list = [c for c in "abcdefghijklmnopqrstuwvxyz"]

answer = "None"
for c in c_list:
  if c not in s_list:
    answer = c
    break

print(answer)