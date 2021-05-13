N = int(input())
L = list(map(int, input().split()))
S = 0
for l in L:
  while l%2==0:
    S += 1
    l = l//2
print(S)