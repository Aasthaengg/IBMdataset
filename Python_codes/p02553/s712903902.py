def a():
  a = list(map(int,input().split()))

  max1 = max(a[0], a[1])
  min1 = min(a[0], a[1])
  max2 = max(a[2], a[3])
  min2 = min(a[2], a[3])
  result = [max1 * max2, max1 * min2, min1 * max2, min1 * min2]

  return max(result)

if __name__ == '__main__':
  print(a())