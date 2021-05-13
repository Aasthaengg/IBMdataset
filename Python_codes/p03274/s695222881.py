n,k = map(int,input().split())
l = list(map(int,input().split()))
m = 10**9
for i in range(n-k+1):
  a = l[i]
  b = l[i+k-1]
  m = min(m,b-a+min(abs(a),abs(b)))
print(m)