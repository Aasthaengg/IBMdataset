N, K = map(int, input().split())
l = list(map(int,input().split()))

l.sort(reverse=True)

snake = 0

for i in range(K):
  snake = snake + l[i]

print(snake)
