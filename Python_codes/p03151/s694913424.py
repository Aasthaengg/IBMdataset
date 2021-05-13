def resolve():
  n = int(input())
  a = list(map(int, input().split()))
  b = list(map(int, input().split()))

  if sum(a) < sum(b):
    print(-1)
    return

  more = []
  less = []

  for i in range(n):
    if a[i] > b[i]:
      more.append(a[i]-b[i])
    elif a[i] < b[i]:
      less.append(b[i]-a[i])

  if len(less) == 0:
    print(0)
    return

  ans = len(less)

  v = sum(less)
  more.sort(reverse=True)
  for i in range(len(more)):
    if v <= 0:
      break
    v -= more[i]
    ans += 1

  print(ans)

  return

if __name__ == "__main__":
  resolve()
