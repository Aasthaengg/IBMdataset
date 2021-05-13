n = int(input())
a_list = list(map(int, input().split()))
count = 0

for a in a_list[::2]:
  if a & 1:
    count += 1
print(count)