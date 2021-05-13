N = int(input())
a = list(map(int,input().split()))
a.append(0)
ans = 0
for i in range(N-1):
  if a[i] == a[i+1]:
    ans += 1
    a[i+1] = max(a[i],a[i+2])+1
print(ans)