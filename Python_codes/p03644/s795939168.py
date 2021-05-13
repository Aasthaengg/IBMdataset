N = int(input())
for i in range(10):
  if 2**i <= N and 2**(i+1) > N:
    ans = 2**i
    break
print(ans)