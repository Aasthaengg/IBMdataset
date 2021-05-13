N,A,B = map(int, input().split(" "))
distance = abs(B - A)
res=0
if distance % 2 == 0:
  res = distance//2
else:
  res = distance//2 + min(min(A,B)-1, N-max(A,B))+1
print(res)