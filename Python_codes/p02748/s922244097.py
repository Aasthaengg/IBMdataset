A,B,M = map(int,input().split())
AA = map(int,input().split())
AAA = list(AA)
BB = map(int,input().split())
BBB = list(BB)
mini = min(AAA) + min(BBB)
for i in range(M):
  x,y,c = map(int,input().split())
  xxx = AAA[x-1] + BBB[y-1] - c
  if mini >xxx:
    mini = xxx
print(mini)