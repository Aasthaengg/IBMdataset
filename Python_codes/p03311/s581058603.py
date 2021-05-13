n = int(input())
A = list(map(int, input().split()))
l = sorted([ A[i]-(i+1) for i in range(n) ])
c = 0
m = l[n//2]
for i in l:
  c += abs(i-m)
print(c)