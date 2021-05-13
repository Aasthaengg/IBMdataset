A, B, M = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
c = [[int(x) for x in input().split()] for _ in range(M)]
ans = min(a) + min(b)
for i in range(M):
  n_ans = a[c[i][0]-1]+b[c[i][1]-1]-c[i][2]
  ans = min(n_ans, ans)
print(ans)