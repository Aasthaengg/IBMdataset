S = str(input())
V = [S.count('a'),S.count('b'),S.count('c')]
V.sort()
ans = 'YES'
if V[2]-V[0] > 1:
  ans = 'NO'

print(ans)