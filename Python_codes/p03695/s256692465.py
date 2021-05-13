N = int(input())
A = list(map(int,input().split()))
ls = [0]*8
now = 0
for i in range(N):
  if 3200 <= A[i]:
    now += 1
  else:
    ls[A[i]//400] += 1
if 8-ls.count(0) >= 1:
  minimum = 8-ls.count(0)
else:
  minimum = 1
print(minimum,8-ls.count(0)+now)