N = int(input())
ABs = [list(map(int, input().split())) for _ in range(N)]

rlt = 0
for ab in ABs[::-1]:
  ext = (ab[0]+rlt) % ab[1]
  if ext != 0:
    rlt += (ab[1] - ext)
    
print(rlt)