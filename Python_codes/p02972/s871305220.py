n = int(input())
a = [0]+list(map(int,input().split()))
N = [i for i in range(1,n+1)]
N.reverse()
ans = [0]*(n+1)
b = []

for i in N:
  if i*2 > n:
    if a[i] == 1:
      ans[i] = 1
  else:
    if a[i] == 1:
      if sum(ans[i::i])%2 == 0:
        ans[i] = 1
    else:
      if sum(ans[i::i])%2 == 1:
        ans[i] = 1
        
for i in range(1,n+1):
  if ans[i] == 1:
    b.append(i)

print(len(b))
print(*b)