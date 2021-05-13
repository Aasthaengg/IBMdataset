N = int(input())
A = list(map(int,input().split()))

total = 3**N
ng = 1
for a in A:
  if a%2 == 0:
    ng *= 2
print(total-ng)