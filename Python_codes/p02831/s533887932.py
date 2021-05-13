A,B=map(int,input().split())
maxi = max(A,B)
mid = maxi
mini = min(A,B)
res = 0
if A % B ==0 or B % A ==0:
  res = maxi
while res ==0:
  if maxi % mini == 0:
    res = maxi
  maxi += mid
print(res)