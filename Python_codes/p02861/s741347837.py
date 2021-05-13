import itertools

n = int(input())
lst = []
for _ in range(n):
  lst.append(list(map(int, input().split())))
#print(lst)

cases = list(itertools.permutations(list(range(n))))
#print(cases)
length = 0
for case in cases:
  for i in range(n - 1):
    pos_1 = case[i]
    pos_2 = case[i + 1]
    position_1 = lst[pos_1]
    position_2 = lst[pos_2]
    #print(position_1)
    length += ((position_1[0] - position_2[0]) ** 2 + (position_1[1] - position_2[1]) ** 2) ** 0.5
length = length / len(cases)
print(length)