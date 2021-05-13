n, h, w = map(int, input().split())
woods = [list(map(int, input().split())) for i in range(n)]

i = 0
for elm in woods:
  if elm[0] >= h and elm[1] >= w:
    i += 1
  else:
    pass
  
print(i)