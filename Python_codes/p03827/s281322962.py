#32 2020/07/14
N = int(input())
S = list(input())
count = 0
max = 0
for i in range(N):
  if S[i] == 'D':
    count -= 1
  elif S[i] == 'I':
    count += 1
  if count > max:
    max = count
print(max)