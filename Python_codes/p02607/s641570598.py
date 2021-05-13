n = int(input())
a = list(map(int, input().split()))
ans = a[0::2]
cnt = 0

for i in range(len(ans)):
  if (ans[i] % 2) != 0:
    cnt += 1
    
print(cnt)