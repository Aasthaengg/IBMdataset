def f(n, d, points):
  result = 0
  for val in points:
    temp = val[0] * val[0] + val[1] * val[1]
    if d*d >= temp:
      result += 1
  return result

if __name__ == "__main__":
  nd = list(map(int, input().split()))
  n = nd[0]
  d = nd[1]
  points = [list(map(int, input().split())) for _ in range(n)]
  print(f(n, d, points))