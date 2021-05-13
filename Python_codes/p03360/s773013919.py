a = [int(i) for i in input().split()]
K=int(input())
a.sort()
ans = 0
for i in range(K):
  a[-1] *= 2
print(sum(a))