def main():
  n, a, b, c = map(int, input().split())

  l = [int(input()) for i in range(n)]

  def test(i, x, y, z):
    if(i == n):
      if(x == 0 or y == 0 or z == 0):
        return float('inf')
      return abs(a - x) + abs(b - y) + abs(c - z)

    res = test(i + 1, x, y, z)

    res = min(res, (test(i + 1, x + l[i], y, z) + (0 if x == 0 else 10))) 
    res = min(res, (test(i + 1, x, y + l[i], z) + (0 if y == 0 else 10))) 
    res = min(res, (test(i + 1, x, y, z + l[i]) + (0 if z == 0 else 10))) 

    return res

  print(test(0, 0, 0, 0))

if __name__ == '__main__':
  main()
