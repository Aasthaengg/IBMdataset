def main():
  N = int(input())
  A = list(map(int, input().split()))

  ans = 1
  x=y=0
  for i in range(1, N):

    if A[i - 1] < A[i]:
      x = 1

    if A[i - 1] > A[i]:
      y = 1

    if x and y:
      ans += 1
      x = y = 0

  print(ans)

main()
