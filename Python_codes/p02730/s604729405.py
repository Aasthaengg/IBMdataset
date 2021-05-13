s = str(input())
s_len = int((len(s) - 1) / 2)

s_1 = s[:s_len]
s_1_len = int((len(s_1) - 1) / 2)

s_2 = s[s_len+1:]
s_2_len = int((len(s_2) - 1) / 2)

ans = 'Yes'

for i in range(s_len+1):
  if s[i] != s[-i-1]:
    ans = 'No'
    break

for i in range(s_1_len+1):
  if s_1[i] != s_1[-i-1]:
    ans = 'No'
    break

for i in range(s_2_len+1):
  if s_2[i] != s_2[-i-1]:
    ans = 'No'
    break

print(ans)