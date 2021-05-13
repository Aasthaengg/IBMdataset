dollar = int(input())
max_7 = dollar//7+1
for i in range(max_7):
  amari = dollar - 7*i
  if amari % 4==0:
    print('Yes')
    break
  if i==max_7-1:
    print('No')