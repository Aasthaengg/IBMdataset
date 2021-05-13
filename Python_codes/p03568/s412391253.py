N = int(input())
a = list(map(int,input().split()))

evencount = 0
for i in range(N):
  if a[i]%2 == 0:
    evencount += 1

print(3**N-2**evencount)