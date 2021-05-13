N, A, B = map(int, input().split())

if A > B:
  max = B
else:
  max = A

if A + B > N:
  min = A + B - N
else:
  min = 0
  
print(max, min)