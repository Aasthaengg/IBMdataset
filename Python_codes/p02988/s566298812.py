n = int(input())
p = list(map(int, input().split()))

def checkP(int1, int2, int3):
  l = [int1, int2, int3]
  l.sort()
  if l[1] == int2:
    return True
  else:
    return False

ans = 0

for i in range(1, n-1):
  if checkP(p[i-1], p[i], p[i+1]):
    ans +=1
  else:
    pass

print(ans)