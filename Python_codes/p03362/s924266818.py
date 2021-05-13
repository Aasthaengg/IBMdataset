N = int(input())

fact = [True] * 55556

fact[0],fact[1] = False, False

ans = []
cnt = 0
for i in range(2, len(fact)):
  if fact[i]:
    if i % 5 == 1:
      ans.append(i)
      cnt += 1
      if cnt == N:
        break
    for j in range(i * 2, len(fact), i):
      fact[j] = False

print(*ans)