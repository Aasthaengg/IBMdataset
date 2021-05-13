kk = list(map(int, input().split()))
A, B = kk
answer = []

for p in range(A):
  pp = list(map(int, input().split()))
  C, D = pp
  leng = C*C + D*D
  if leng > B*B:
    answer.append(0)
  else:
    answer.append(1)
    
print(sum(answer))