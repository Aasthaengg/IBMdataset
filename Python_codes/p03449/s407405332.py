def resolve():
  n = int(input())
  a1 = list(map(int, input().split()))
  a2 = list(map(int, input().split()))
  s1 = [0] * (n+1)
  s2 = [0] * (n+1)
  for i in range(n):
    s1[i] = a1[i]
    if i > 0:
      s1[i] += s1[i-1]
  for i in range(n):
    s2[n-i-1] = a2[n-i-1]
    if i > 0:
      s2[n-i-1] += s2[n-i]

  ans = 0
  for i in range(n):
    ans = max(ans, s1[i] + s2[i])

  print(ans)

  return

if __name__ == "__main__":
  resolve()
