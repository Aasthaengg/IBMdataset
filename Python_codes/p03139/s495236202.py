N, A, B = map(int,input().split())
li = [A, B]
if sum(li)<=N:
  a = 0
else:
  a = sum(li)-N
print(min(li),a)