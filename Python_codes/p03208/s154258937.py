N,K = map(int, input().split())
h = []
for _ in range(N):
    h.append(int(input()))
h = sorted(h)
list =[]
for i in range(N-K+1):
  list.append(h[i+K-1]-h[i])
list = sorted(list)
print(list[0])