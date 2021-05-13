n,m = map(int, input().split())
l = list(map(int, input().split()))
c = 0
for i in l:
  c += i
print(n-c if n-c >= 0 else -1)