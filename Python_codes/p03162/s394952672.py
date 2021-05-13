N = int(input())
Da = [0 for i in range(N+1)]
Db = [0 for i in range(N+1)]
Dc = [0 for i in range(N+1)]
for i in range(1, N+1):
  a, b, c = map(int, input().split())
  Da[i] = max(Db[i-1], Dc[i-1]) + a
  Db[i] = max(Da[i-1], Dc[i-1]) + b
  Dc[i] = max(Da[i-1], Db[i-1]) + c
print(max(Da[N], Db[N], Dc[N]))