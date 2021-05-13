N = int(input())
length = list(map(int,input().split()))
if max(length)*2 < sum(length):
  print('Yes')
else:
  print('No')