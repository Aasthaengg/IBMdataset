A, B = map(int, input().split())

count = 0
for i in range(A, B+1):
  i_str = str(i)
  i_reversed_str = str(i)[::-1]
  if i_str == i_reversed_str:
    count += 1

print(count)