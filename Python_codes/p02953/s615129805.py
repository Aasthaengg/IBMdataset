n = int(input())
a = list(map(int,input().split()))
m = 0
for i in range(n):
  m = max(m,a[i])
  if a[i] < m-1:
    print("No")
    exit()
print("Yes")