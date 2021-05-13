def main():
  N = int(input())
  A = list(map(int,input().split()))
  tmp = 1
  for i in range(N):
    if A[i] % 2 == 0:
      tmp *= 2  
  print(3**N - tmp)
main()  