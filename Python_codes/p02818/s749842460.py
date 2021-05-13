A, B, K= map(int, input().split())
 
if A >= K:
  ans_t = A - K
  ans_a = B
elif B >= ( K - A):
  ans_t = 0
  ans_a = B - ( K - A)
else:
  ans_t = 0
  ans_a = 0
 
print( '{} {}'.format( ans_t, ans_a))