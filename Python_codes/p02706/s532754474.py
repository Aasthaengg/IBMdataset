def main():
 n, m = map(int,input().split())
 a = list(map(int,input().split()))
 Sum = sum(a)
 if Sum <= n:
  print(n - Sum)
 else:
  print(-1)
      
main()
