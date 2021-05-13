a = []
for _ in range(3):
  a = a + [int(i) for i in input().split()]
n = int(input())
a_bingo = [0] * 3 * 3
pos = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
for _ in range(n):
  b = int(input())
  if b in a:
    a_bingo[a.index(b)] = 1
for po in pos:
  if a_bingo[po[0]] == a_bingo[po[1]] == a_bingo[po[2]] == 1:
    print('Yes')
    exit()
print('No')