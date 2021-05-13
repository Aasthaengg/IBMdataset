start, end, div = list(map(int, input().strip().split()))

count = end // div - start //div

if start % div == 0:
  count += 1
print(count)