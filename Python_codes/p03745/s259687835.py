N = int(input())
L = list(map(int, input().split()))

ans1 = 1
flag = ''
for i in range(1, N):
  if flag == '':
    if L[i] < L[i-1]:
      flag = 'minus'
    elif L[i] > L[i-1]:
      flag = 'plus'
    else:
      flag = ''

  if flag == 'plus':
    if L[i] < L[i-1]:
      flag = ''
      ans1 += 1
  elif flag == 'minus':
    if L[i] > L[i-1]:
      flag = ''
      ans1 += 1


print(ans1)