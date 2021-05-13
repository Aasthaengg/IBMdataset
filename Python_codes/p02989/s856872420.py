N = int(input())
N2 = int(N/2)
d = [int(x) for x in input().split()]
d.sort()

if d[N2-1] == d[N2]:
  K = 0
else:
  K = d[N2] - d[N2-1]
  
print(K)