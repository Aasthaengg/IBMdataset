n = int(input())
h = [ list(map(int,input().split())) for _ in range(n)]

ans = []
for i in range(101):
  for j in range(101):
    h.sort(key=lambda x: -x[2])
    hmax = h[0][2] + abs(i-h[0][0]) + abs(j-h[0][1])
    for k in range(1,n):

      if max(hmax - abs(h[k][0] - i) - abs(h[k][1] - j) , 0) != h[k][2]:
        break

    else:
      ans = [i,j,hmax]
    
    if(len(ans)):
      break
  if(len(ans)):
    break

ans = map(str,ans)
print(' '.join(ans))