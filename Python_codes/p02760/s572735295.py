bin = []
for i in range(3):
  bin.append(list(map(int, input().split())))
bin = sum(bin, [])
N = int(input())
bingo = [False for _ in range(9)]
for _ in range(N):
  b = int(input())
  if b in bin:
    bingo[bin.index(b)] = True
if (bingo[0] and bingo[1] and bingo[2]) or (bingo[3] and bingo[4] and bingo[5]) or \
   (bingo[6] and bingo[7] and bingo[8]) or (bingo[0] and bingo[3] and bingo[6]) or \
   (bingo[1] and bingo[4] and bingo[7]) or (bingo[2] and bingo[5] and bingo[8]) or \
   (bingo[0] and bingo[4] and bingo[8]) or (bingo[2] and bingo[4] and bingo[6]):
  print("Yes")
else:
  print("No")