x=int(input())
k=100
cnt=0
while k<x:
  k += k // 100
  cnt += 1

print(cnt)