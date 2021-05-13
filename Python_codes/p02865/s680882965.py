N = int(input())
ans = []
for i in range(1, N//2+1):
  if i != (N-i):
    ans.append((i, N-i))
print(len(set(ans)))