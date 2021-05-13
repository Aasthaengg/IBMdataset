H, W = map(int, input().split())
S = [input() for _ in range(H)]
D = {}
center_of_center = (H % 2) * (W % 2)
center_of_H = (H % 2) * (W >> 1)
center_of_W = (W % 2) * (H >> 1)
for i in range(H):
  for j in range(W):
    if S[i][j] in D:
      D[S[i][j]] += 1
    else:
      D[S[i][j]] = 1
odd, half_odd, four = 0, 0, 0
odds = []
half_odds = []
fours = []
for i in D:
  if D[i] % 2:
    odd += 1
    odds.append(i)
  else:
    if (D[i] >> 1) % 2:
      half_odds.append(i)
      half_odd += 1
    else:
      four += 1
      fours.append(i)
if odd != center_of_center:
  print("No")
else:
  if odd != 0:
    D[odds[0]] -= 1
    if D[odds[0]] % 4 == 2:
      half_odd += 1
    else:
      four += 1
  if (center_of_H + center_of_W) % 2 != half_odd % 2 or center_of_H + center_of_W < half_odd:
    print("No")
  else:
    print("Yes")