n = int(input())
A = list(map(int, input().split()))
cnt = 0
for a in A:
  if a%2==0:
    while a%2==0:
      a //= 2
      cnt += 1
print(cnt)