N = int(input())
R = []

for n in range(N):
  s,p = input().split()
  R.append((s,-int(p),n+1))
  
for s,p,n in sorted(R):
  print(n)
