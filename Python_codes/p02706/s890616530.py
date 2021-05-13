def main():
 n, m = map(int,input().split())
 a = list(map(int,input().split()))
 sum = 0
 for i in a:
  sum += i
 if sum <= n:
  print(n - sum)
 else:
  print(-1)
      
main()