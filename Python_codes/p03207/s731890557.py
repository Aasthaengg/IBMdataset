N = int(input())
ls = []
for i in range(N):
  ls.append(int(input()))
ls.sort()
print(ls[N-1] // 2 + sum(ls[0:N-1]))