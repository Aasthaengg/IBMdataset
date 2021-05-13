N = int(input())
H = list(map(int, input().split()))
c,m = 0,0 
for i in range(N-1):
  if H[i]>=H[i+1]:
    c += 1
    m = max(c,m)
  else:
    c = 0
print(m)