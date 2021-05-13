def main():
  n, a, b, c, d = map(int, input().split())
  s = input()
  possible = True
  cnt = 0
  for i in range(a-1, c):
    if s[i] == ".":
      cnt = 0
    else:
      cnt += 1
    if cnt > 1:
      possible = False
      break
  cnt = 0
  for i in range(b-1, d):
    if s[i] == ".":
      cnt = 0
    else:
      cnt += 1
    if cnt > 1:
      possible = False
      break    
  if c > d:
    cnt = 0
    for i in range(b-2, d+1):
      if s[i] == "#":
        cnt = 0
      else:
        cnt += 1
      if cnt >= 3:
        break
    else:
      possible = False
  print("Yes" if possible else "No")


if __name__ == "__main__":
  main()
