def main():
  N = int(input())
  A = list(map(int, input().split()))
  A = sorted(A, reverse = True)
  flag = True
  num = 0
  ans = 1
  for i in range(N-1):
    if A[i] == A[i+1] and flag:
      ans *= A[i]
      num += 1
      if num == 2:
        break
      flag = False
    elif not flag:
      flag = True
  if num < 2:
    ans = 0
  print(ans)
main()