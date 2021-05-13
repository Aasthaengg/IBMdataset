def main():
  n=int(input())
  A=[int(input()) for i in range(n)]
  crt=1
  cnt=0
  for i in range(n):
    cnt += 1
    crt = A[crt-1]
    if crt == 2:
      print(cnt)
      break
  else:
    print(-1)
main()