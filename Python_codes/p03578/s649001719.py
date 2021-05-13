N = int(input())
L = list(map(int, input().split()))
M = int(input())
T = list(map(int, input().split()))

dic = {}
for i in range(N):
  if L[i] in dic:
    dic[L[i]] += 1
  else:
    dic[L[i]] = 1

ans = 'YES'
for i in range(M):
  if T[i] in dic:
    if dic[T[i]] > 0:
      dic[T[i]] -= 1
    else:
      ans = 'NO'
      break
  else:
    ans = 'NO'
    break

print(ans)

