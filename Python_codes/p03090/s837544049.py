N=int(input())

# Nが奇数の場合、(N-自分)に対しては辺を貼らない
# Nが偶数の場合、(N+1-自分)に対しては辺を貼らない

ans = []
odd = (N%2 == 1)
def needs_edge(i,j,N,odd):
  if odd:
    if N-i == j:
      return False
  else:
    if N+1-i == j:
      return False
  return True

for i in range(1,N):
  for j in range(i+1,N+1):
    if needs_edge(i,j,N,odd):
      ans.append([i,j])

print(len(ans))
for a in ans:
  print(*a)
