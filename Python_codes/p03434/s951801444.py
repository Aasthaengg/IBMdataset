import math

N = input()
num_list = list(map(int,input().split(' ')))
i = 0
Bob = 0
Alice = 0
for n in sorted(num_list, reverse=True):
  i += 1
  if i % 2 == 1:
    Bob += n
  elif i % 2 == 0:
    Alice += n
ans = Bob - Alice
print(ans)