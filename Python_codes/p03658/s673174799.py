n, k = map(int, input().split())
l = list(map(int, input().split()))

l.sort(reverse = True)
ans = []
for i in range(k):
  ans.append(l[i])
  
print(sum(ans))