n , m = map(int , input().split())
ans = [0] * n
for i in range(m):
  inp = list(map(int , input().split()))
  ans[inp[0] - 1] += 1
  ans[inp[1] - 1] += 1
print('\n'.join([str(n) for n in ans]))