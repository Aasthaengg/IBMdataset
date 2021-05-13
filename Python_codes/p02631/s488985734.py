n = int(input())
a_lst = list(map(int, input().split()))

all_ = 0
for a in a_lst:
  all_ = all_ ^ a

for a in a_lst:
  print(all_ ^ a, end=' ')