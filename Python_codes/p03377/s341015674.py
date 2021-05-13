A,B,X = map(int, input().split())

_ = X-A
if (_ >= 0) and (_ <= B):
  ans = 'YES'
else:
  ans = 'NO'

print(ans)