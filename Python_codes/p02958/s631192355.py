n = int(input())
p = list(map(int, input().split()))
l = [i for i in range(1,n+1)]
c = 0
for j in range(n):
  if p[j] != l[j]:
    c += 1
print("YES" if c == 0 or c == 2 else "NO")