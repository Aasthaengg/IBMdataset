a,b,k=map(int,input().split())
m = min(a,b)
l = set()
for i in range(1,m+1):
  if a%i == 0 and b%i == 0:
    l.add(i)

print(sorted(list(l))[-k])