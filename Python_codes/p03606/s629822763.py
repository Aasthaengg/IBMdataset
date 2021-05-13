N  = int(input())
n=[]
for i in range(N):
  l, r = map(int, input().split())
  a = r - l + 1
  n.append(int(a))
print(sum(n))