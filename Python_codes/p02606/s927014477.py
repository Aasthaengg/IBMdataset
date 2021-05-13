L, R, d = list(map(int, input().split(" ")))

diff=R//d - (L-1)//d

if d==1:
  diff=diff

print(diff)