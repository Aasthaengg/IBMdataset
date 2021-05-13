inf = 10**9


def calcDistance(p1,p2):
  return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def calcNearestCheckpoints(person,checkpoints):
  ans = -1
  min_distance = inf
  for i in range(len(checkpoints)):
    distance = calcDistance(person,checkpoints[i])
    if distance < min_distance:
      ans = i+1
      min_distance = distance

  return ans

def main():
  N,M = map(int,input().split())
  people      = [list(map(int,input().split())) for _ in range(N)]
  checkpoints = [list(map(int,input().split())) for _ in range(M)]
  for i in range(N):
    person = people[i]
    print(calcNearestCheckpoints(person,checkpoints))

main()
