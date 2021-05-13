n, k = map(int, input().split())
length = list(map(int, input().split()))

length.sort(reverse=True)
total = 0
for i in range(k):
  total += length[i]

print(total)