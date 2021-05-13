a, b, c = map(int, input().split())

num_lists = [a, b, c]
maximum = a
if maximum < b: maximum = b
if maximum < c: maximum = c

max_index = num_lists.index(maximum)
num_lists.pop(max_index)

remainder = num_lists[0] + num_lists[1]
if maximum == remainder:
  ans = 'Yes'
else:
  ans = 'No'
  
print(ans)