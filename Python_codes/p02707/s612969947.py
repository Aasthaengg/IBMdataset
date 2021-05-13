from collections import Counter

N = int(input())

S = list(map(int, input().split()))

manager_dict = Counter(S)
for i in range(1, N + 1):
  print(manager_dict[i])