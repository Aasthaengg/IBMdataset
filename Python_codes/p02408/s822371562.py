NumberOfSheet = int(input())
OwnedCards = [[str(i) for i in input().split()] for loop in range(NumberOfSheet)]
S = [int(0) for i in range(13)]
H = [int(0) for i in range(13)]
C = [int(0) for i in range(13)]
D = [int(0) for i in range(13)]
for i in OwnedCards:
  if i[0] == 'S' or i[0] == 'H' or i[0] == 'C' or i[0] == 'D':
    if i[0] == 'S': S[int(i[1]) - 1] = 1
    if i[0] == 'H': H[int(i[1]) - 1] = 1
    if i[0] == 'C': C[int(i[1]) - 1] = 1
    if i[0] == 'D': D[int(i[1]) - 1] = 1

for i in range(13):
  if S[i] == 0: print('S',i + 1)
for i in range(13):
  if H[i] == 0: print('H',i + 1)
for i in range(13):
  if C[i] == 0: print('C',i + 1)
for i in range(13):
  if D[i] == 0: print('D',i + 1)