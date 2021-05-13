n = int(input())
bit = -1
l = list(map(int,input().split()))
ans = 0
for i in range(1,n):
  if l[i] == l[i-1]:
    l[i] = bit
    ans += 1
print(ans)