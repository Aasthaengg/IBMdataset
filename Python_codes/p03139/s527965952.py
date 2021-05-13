a,b,c = map(int,input().split())
ans_max = min(b,c)
ans_min = min(b,c)-(a-max(b,c))
if ans_min < 0:
  ans_min = 0
print(ans_max,ans_min)