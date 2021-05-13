N = int(input())

if N % 2 == 0:
  ans = (N//2) / N
else:
  ans = ((N//2)+1) / N

print(ans)