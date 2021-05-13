n = int(input())
l = list(map(int,input().split()))
ans = 0
for i in range(len(l)):
  for j in range(i+1,len(l)):
    for k in range(j+1,len(l)):
      if l[i] != l[j] and l[j] != l[k] and l[k] != l[i]:
        a = [l[i],l[j],l[k]]
        a.sort()
        if a[0]+a[1] > a[2]:
          ans += 1
print(ans)