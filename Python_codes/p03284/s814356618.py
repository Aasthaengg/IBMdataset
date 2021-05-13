N, K = map(int, input().split())

a = [0] * K

for i in range(N):
  a[i%K] +=1

print(max(a) - min(a))