N, K = map(int, input().split())
length = list(map(int, input().split()))
max_length = 0

length.sort(reverse=True)
for i in range(K):
  max_length += length[i]
  
print(max_length)