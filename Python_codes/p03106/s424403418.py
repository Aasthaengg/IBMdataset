A, B, K = map(int, input().split())
c = 0
for i in range(min(A,B), 0, -1):
  if A % i == 0 and B % i == 0:
    c += 1
#    print(c,i)
    if c == K:
      ans = i
print(ans)