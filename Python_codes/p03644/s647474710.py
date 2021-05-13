N = int(input())
ans = 1

for n in range(N):
  ans*=2
  if ans>N:
    print(int(ans/2))
    exit()