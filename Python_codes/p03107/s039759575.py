S = input()
length = len(S)
count_0 = 0
for i in range(length):
  if S[i] == '0':
    count_0 += 1
res = min(count_0, length - count_0) * 2
print(res)