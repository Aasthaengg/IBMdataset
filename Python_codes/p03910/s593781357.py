N = int(input())

now = 0
sum = 0
ans = []
while sum < N:
  now += 1
  ans.append(now)
  sum += now

rem = sum-N
if rem != 0:
  ans.remove(rem)
print(*ans,sep="\n")