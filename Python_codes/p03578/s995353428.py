n = int(input())
D = sorted(list(map(int,input().split())))
m = int(input())
T = sorted(list(map(int,input().split())))

ans = 'YES'
di = -1
for t in T:
  while True:
    di += 1
    if di >= n:
      ans = 'NO'
      break    
    if D[di] == t:
      break
        
print(ans)    