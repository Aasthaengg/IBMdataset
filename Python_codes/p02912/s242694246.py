from bisect import bisect

N,M = map(int,input().split())
Ali = list(map(int,input().split()))

Ali.sort()
for i in range(M):
  a = Ali.pop(-1)
  a //= 2
  Ali.insert(bisect(Ali,a), a)

print(sum(Ali))