N = int(input())
A = list(map(int,input().split()))

odd_count = 1

for a in A:
  if a%2 != 0:
    odd_count *= 1
  else:
    odd_count *= 2

print(3**N - odd_count)