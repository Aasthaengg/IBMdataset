n=int(input())
a=list(map(int,input().split()))
a = [None] + a
cnt = 0
for i in range(1, n):
  j = a[i]
  if j > i and a[j] == i:
    cnt += 1
print(cnt)