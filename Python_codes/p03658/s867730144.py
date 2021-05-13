N,K = map(int,input().split())
l = list(map(int,input().split()))
l = sorted(l)[::-1]
s = 0
for i in range(K):
  s = s + l.pop(0)
print(str(s))