N, T = map(int, input().split())
t = [int(i) for i in input().split()]
count = 0
for i in range(1,N):
  count += min(T, t[i]-t[i-1])
count += T
print(count)
