N = int(input())
B = list(map(int, input().split()))
#flag = True
ans = B[0]
before = B[0]
for k in range(N-1):
  if before > B[k]:
    ans -= before
    ans += B[k]+B[k]
    before = B[k]
  else:
    ans += B[k]
    before = B[k]
print(ans)
#print('Yes')
#print('No')