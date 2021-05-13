def main():
  n = int(input())
  data_ = list(map(int, input().split()))

  # can not divide 2       : 1
  # divide 2 by once       : 2
  # divide 2 by over twice : 4
  data = []
  for d in data_:
    if d % 2 == 1:
      data.append(1)
    else:
      tmp = int(d / 2)
      if tmp % 2 == 1:
        data.append(2)
      else:
        data.append(4)

  # 2が存在しないとき
  if data.count(2) == 0:
    if data.count(1) <= data.count(4) + 1:
      print("Yes")
      return
    else:
      print("No")
      return

  if data.count(1) <= data.count(4):
    print("Yes")
  else:
    print("No")

if __name__ == "__main__":
  main()