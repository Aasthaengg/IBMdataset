if __name__ == "__main__":
  a, b, c = map(int,input().split())
  ans = 3
  if a == b and b == c:
    print("1")
    exit()
  if a == b or b == c or c == a:
    print("2")
    exit()
  print("3")
