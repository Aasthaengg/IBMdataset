n = int(input())
s = input()
turn = [0]
for i in range(n):
  if s[i] == 'W':
    turn.append(turn[-1] + 1)
  else:
    turn.append(turn[-1])
ans = n
for i in range(n):
  ans = min(ans, turn[i] + n - 1 - i - turn[n] + turn[i + 1])
print(ans)
