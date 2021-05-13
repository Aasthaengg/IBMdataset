def main():
  N, M = map(int,input().split())
  sc = list(list(input().split()) for _ in range(M))

  li = [""] * N

  for i in range(M):
    j = li[int(sc[i][0]) - 1]
    if j == "": li[int(sc[i][0]) - 1] = sc[i][1]
    elif j != sc[i][1]: return -1

  for i in range(N):
    if i == 0:
      if li[0] == "0" and N != 1: return -1
      if li[0] == "":
        if N == 1: li[0] = "0"
        else: li[0] = "1"
    elif li[i] == "": li[i] = "0"

  return "".join(li)

print(main())