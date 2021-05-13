N, K = map(int, input().split())
l = sorted(list(map(int, input().split())), reverse=True)
length = 0
for i in range(K):
  length += l[i]

print(length)