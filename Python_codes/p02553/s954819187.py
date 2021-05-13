if __name__ == "__main__":
  a, b, c, d = [int(a) for a in input().split()]
  # x = max(a, b)
  # y = max(c, d)
  # if (x < 0 and y < 0 ) or (x >= 0 and y >= 0):
  #   pass
  # elif x > 0 and y <= 0:
  #   x = min(a, b)
  # elif y > 0 and x <= 0:
  #   y = min(c, d)
  # ret = x * y
  print(max(a*c, a*d, b*c, b*d))
