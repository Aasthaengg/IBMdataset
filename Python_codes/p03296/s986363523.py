N = int(input())
a = list(map(int,input().split()))
count = 0
INF = 10**9
for i in range(1,N):
  if a[i] == a[i-1]:
    a[i] = INF
    count += 1
print(count)