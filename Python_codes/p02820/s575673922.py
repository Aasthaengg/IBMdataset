N, K = map(int, input().split())
scores = list(map(int, input().split()))
tables = {'s': 0, 'p': 1, 'r': 2}

patterns = input()
answer = 0
losers = [0 for _ in range(N)]
for i in range(N):
  if i - K < 0:
    answer += scores[tables[patterns[i]]]
  else:
    if patterns[i] == patterns[i-K]:
      if losers[i-K] == 0:
        losers[i] = 1
      else:
        answer += scores[tables[patterns[i]]]
    else:
      answer += scores[tables[patterns[i]]]
print(answer)