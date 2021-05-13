N = int(input())
mass = list(map(int, input().split()))
odd_list = []
count = 0
for i in range(0, len(mass), 2):
  odd_list.append(mass[i])
for k in odd_list:
  if k % 2 != 0:
    count += 1
print(count)