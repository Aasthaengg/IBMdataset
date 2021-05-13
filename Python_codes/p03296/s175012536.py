n = int(input())
s = list(map(int, input().split()))

cnt = 1
res = 0
for i in range(1, n):
  if s[i] == s[i-1]:
    cnt +=1
  else:
    res += int(cnt//2)
    cnt = 1
res += int(cnt//2)

print(res)