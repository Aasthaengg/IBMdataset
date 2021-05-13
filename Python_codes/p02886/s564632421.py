N = int(input())
dd = input().split()
total = 0
for i in range(N-1):
  for j in range(i+1,N):
    total += int(dd[i]) * int(dd[j])
print(total)