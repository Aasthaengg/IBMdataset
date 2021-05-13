N = int(input())
T,A=map(int,input().split())
List = list(map(int, input().split()))
t = 0
mid = 0
MID = 100000000000
res = 100000000000
for i in range(N):
  t = T - 0.006*List[i]
  mid = abs(A-t)
  if mid < MID:
    MID = mid
    res = i+1
print(res)