R, G, B, N = map(int, input().split())

answer = 0
for r in range(N//R+1):
  for g in range(N//G+1):
    if r*R + g*G > N:
      break
    elif (N-r*R-g*G)%B != 0:
      continue
    else:
      answer += 1
print(answer)
