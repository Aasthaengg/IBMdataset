N = int(input())
S = input()

Alpha = list('ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ')
ans = ''

for i in S:
  ans += Alpha[Alpha.index(i) + N]
  
print(ans)