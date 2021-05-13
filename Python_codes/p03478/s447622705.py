N,A,B = map(int,input().split())
ans=0

for i in range(0,N+1):
  keta_sum = 0
  i = str(i)
  for j in range(len(str(i))):
    keta_sum += int(i[j])
  if A <= keta_sum <= B:
    ans += int(i)

print(ans)