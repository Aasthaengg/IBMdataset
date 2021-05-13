N=int(input())
count=0
for i in range(N):
  sp,ep=map(int, input().split())
  count+=ep-sp+1
print(count)