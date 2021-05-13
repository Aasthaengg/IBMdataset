N, M = list(map(int,input().split()))
a = []
for i in range(M):
    a.append(list(map(int,input().split())))
a = sorted(a, key=lambda x: x[1])
left = -1
ans = 0
for i in range(M):
    if left < a[i][0]:
      left = a[i][1] - 1
      ans += 1
print(ans)