n, c = map(int, input().split())
list_rec = [[0] * 10**5 for _ in range(c)]

list_tv = [tuple(map(int, input().split())) for _ in range(n)]
for start, end, ch in list_tv:
  list_rec[ch-1][(start-1):end] = [1] * (end - (start - 1))

count = max(map(sum, zip(*list_rec)))
print(count)