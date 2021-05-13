A, B, C = map(int, input().split())
cnt = 0
while True:
  if A%2!=0 or B%2!=0 or C%2!=0:
    print(cnt)
    break
  elif A == B and B == C and A == C:
    print(-1)
    break
  else:
    temp_A = A
    temp_B = B
    A = B/2 + C/2
    B = temp_A/2 + C/2
    C = temp_A/2 + temp_B/2
    cnt += 1