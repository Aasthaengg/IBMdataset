N, A, B = map(int,input().split())

ans = 0
for n in range(N+1):
  sums = sum(list(map(int,list(str(n)))))
  if A <= sums and sums <= B:
    ans += n

print(ans)