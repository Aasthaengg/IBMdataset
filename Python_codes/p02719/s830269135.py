N,K = map(int,input().split())

a = N//K
b = abs(N-(a+1)*K)

if N - a*K <= b:
  print(N-a*K)
elif N - a*K > b:
  print(b)