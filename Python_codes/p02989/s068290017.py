N = int(input())
d = list(map(int,input().split()))
d = sorted(d)

if len(d) % 2 == 1:
  print(0)
  exit(0)
  
pick = len(d)//2
ans = d[pick] - d[pick-1]
print(ans)
