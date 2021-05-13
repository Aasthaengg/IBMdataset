n = int(input())

num_lists = list(range(1, n+1, 1))
count = 1
while len(num_lists) != 1:
  num_lists = [i for i in num_lists if i%2**count == 0]
  count += 1
print(num_lists[0])