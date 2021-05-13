N = int(input())
A = []
for i in range(N):
  A.append(int(input()))
#print(A)

ans = 0
pre = 0
maxa = 0
for i in range(N):
  if A[i] > maxa:
    print(-1)
    exit()
  else:
    if A[i] == 0:
      maxa = 0
    elif A[i] == pre + 1:
      ans += 1
    else:
      ans += A[i]
      maxa = A[i]
    pre = A[i]
    maxa += 1
print(ans)
