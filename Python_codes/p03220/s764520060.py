N = int(input())
T, A = list(map(int, input().split(" ")))
H = list(map(int, input().split(" ")))

def getTemperature(H):
  return T - H * 0.006

def adjustAbs(H):
  if H > A:
    return abs(H - A)
  else:
    return abs(A - H)

H = list(map(getTemperature, H))

H = list(map(adjustAbs, H))

print(H.index(min(H))+1)