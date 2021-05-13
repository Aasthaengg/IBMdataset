
s = input()
K = int(input())
len_s = len(s)

result = []

for i in range(len_s):
  for j in range(i+1, i+1+5):
    x = s[i:j]
    result.append(x)

result = sorted(result)
len_r = len(result)

if len_r == 1 or K == 1:
  print(result[0])
  exit()

index = 0
for i in range(1, len_r):
  if result[i] != result[i-1]:
    index += 1
  if index == K-1:
    print(result[i])
    exit()