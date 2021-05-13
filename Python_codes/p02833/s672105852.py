N = int(input())

if N%2 == 1:
  print("0")
  exit(0)

N = N//2
ans = 0  
while N > 1:
  N = N//5
  ans += N
print(ans)