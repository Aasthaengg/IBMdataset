N, X = map(int, input().split())
l = [0] + list(map(int, input().split()))
d = [0]

for i in range(1, N+1):
    d.append(d[-1]+l[i])

cnt = 0
for i in d:
    if i <= X:
      cnt += 1
print(cnt)