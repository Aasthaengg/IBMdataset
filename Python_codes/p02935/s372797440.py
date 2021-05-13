N = int(input())
V = input().split(' ')
V = [int(V[i]) for i in range(N)]
V = sorted(V)
count = V[0]
for i in range(1, N, 1):
  count = (count + V[i])/2
print(count)