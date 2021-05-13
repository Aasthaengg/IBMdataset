x, n = map(int, input().split())
l = list(map(int, input().split()))

sa = 0


while(True):
  if x - sa not in l:
    ans = x - sa
    break
    
  elif x +sa not in l:
    ans = x + sa
    break
  else:
    sa +=1
print(ans)