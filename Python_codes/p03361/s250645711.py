h, w = map(int, input().split())
s = [['.'] * (w + 2) ]
for _ in range(h):
  s.append(['.'] + list(input()) + ['.'])
s.append(['.'] * (w + 2))
for y in range(1, h + 1):
  for x in range(1, w + 1):
    if s[y][x]=="#" and s[y-1][x]=="." and s[y+1][x]=="." and s[y][x-1]=="." and s[y][x+1]==".":
        print("No")
        exit()
print("Yes")